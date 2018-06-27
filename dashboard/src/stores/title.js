import TitleActions from '../actions/title';
import alt from '../alt';

class TitleStore {
  constructor() {
    this.bindActions(TitleActions);

    this.title = '';
  }

  onSetTitle(title) {
    return this.setState({
      title
    });
  }
}

export default alt.createStore(TitleStore);