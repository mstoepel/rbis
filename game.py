import time
from threading import Thread

from simulation import BaseObject, Ship
from simulation.systems import Planet, SolarSystem


class Game(BaseObject):
    def __init__(self):
        super().__init__()

        self.objects = []
        self.running = False

        self._socket = None

        Thread(target=self.run, args=(), daemon=True).start()
        Thread(target=self.monitor, args=(), daemon=True).start()

    def set_socket(self, socket):
        self._socket = socket

    def close_socket(self):
        self._socket = None

    def stop(self):
        self.running = False

    def start(self):
        self.running = True

    def restart(self):
        # TODO: Set universe state back to beginning, same generated world?
        self.running = True

    def monitor(self):
        last_check_time = time.time()

        while True:
            current_time = time.time()

            sleep_time = 1. - (current_time - last_check_time)
            if sleep_time > 0:
                time.sleep(sleep_time)

            if self._socket:
                self._socket.write_message(self.dump())

            last_check_time = time.time()

    def run(self):
        last_frame_time = time.time()

        while True:
            # dt is the time delta in seconds (float).
            current_time = time.time()

            sleep_time = 1. - (current_time - last_frame_time)
            if sleep_time > 0:
                time.sleep(sleep_time)

            dt = time.time() - last_frame_time

            # Run the simulation update
            if self.running:
                self.update(dt)

            last_frame_time = time.time()

    def generate(self):
        self.objects = []

        system = SolarSystem(name='Andromeda')
        planet1 = Planet('planet1', system, 100, 2000, 50, 100)
        planet2 = Planet('planet2', system, 50, 1000, 20, 10)

        system.add_planet(planet1)

        system.add_planet(planet2)

        self.objects.append(system)

        self.objects.append(
            Ship(
                system,
                0,
                -50
            )
        )

        self.objects.append(
            Ship(
                system,
                0,
                50
            )
        )

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def __getstate__(self):
        """
        Customize what gets pickled

        :return:
        """
        state = self.__dict__.copy()
        del state['_socket']
        return state
