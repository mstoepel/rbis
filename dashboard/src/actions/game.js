import alt from '../alt';

class GameActions {
  constructor() {
    this.generateActions('connect', 'disconnect', 'start', 'stop', 'restart', 'generate');
  }
}

export default alt.createActions(GameActions);
