import alt from '../alt';

class TitleActions {
  constructor() {
    this.generateActions('setTitle');
  }
}

export default alt.createActions(TitleActions);
