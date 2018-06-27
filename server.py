import json
import os
import sys

import tornado.ioloop
import tornado.web
import tornado.websocket

from game import Game

game = Game()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("dashboard/src/index-server.html")


class SimulationHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("client connected")
        game.set_socket(self)

    def on_message(self, message):
        data = json.loads(message)

        # Check for a method
        if data.get('method'):
            method = data.get('method')
            if hasattr(game, method):
                func = getattr(game, method)
                func()

    def on_close(self):
        print("client disconnected")
        game.close_socket()


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "dashboard", "dist"),
        "cookie_secret": "dsfj9.ugw90i3rkpqj/e;oij2309ir9023r",
    }

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/game", SimulationHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        sys.exit(1)
