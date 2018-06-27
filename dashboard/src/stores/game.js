import GameActions from '../actions/game';
import alt from '../alt';

// Load our simulation classes into the window
import '../simulation/game';
import '../simulation/system';
import '../simulation/ship';

import jsonpickle from 'jsonpicklejs';

class GameStore {
	constructor() {
		this.bindActions(GameActions);

    this.socket = null;
		this.game = {};
		this.status = 'disconnected';
	}

	static getObjectsByType(type) {
    if(!this.getState().game.objects) {
      return [];
    }

	  let returned = [];

    this.getState().game.objects.map((object) => {
      if(object["_py_class"] == type) {
        returned.push(object);
      }
    });

    return returned;
  }

  static getObjectById(id) {
    if(!this.getState().game.objects) {
      return [];
    }

    this.getState().game.objects.map((object) => {
      if(object.id == id) {
        return object;
      }
    });
  }

	onConnect() {
    const url = 'ws://localhost:8080/game';

    this.setState({
      status: 'connecting'
    });

    this.socket = new WebSocket(url);
    this.socket.onopen = this._onOpen;
    this.socket.onclose = this._onClose;
    this.socket.onerror = this._onError;
    this.socket.onmessage = this._onMessage;
  }

  onDisconnect() {
    this.socket.close();
  }

  onStart() {
    this.socket.send(JSON.stringify({
      method: 'start'
    }));
  }

  onStop() {
    this.socket.send(JSON.stringify({
      method: 'stop'
    }));
  }

  onRestart() {
    this.socket.send(JSON.stringify({
      method: 'restart'
    }));
  }

  onGenerate() {
    this.socket.send(JSON.stringify({
      method: 'generate'
    }));
  }

  // Helper functions
  _onOpen = () => {
    this.setState({
      status: 'connected'
    });
  };

  _onClose = () => {
    this.setState({
      status: 'disconnected'
    });
  };

  _onError = () => {
    this.setState({
      status: 'error'
    });
  };

  _onMessage = (raw_message) => {
    const game = jsonpickle.decode(raw_message.data);

    this.setState({
      game
    });
  };
}

export default alt.createStore(GameStore);