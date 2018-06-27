import React, { Component } from 'react';
import connectToStores from 'alt-utils/lib/connectToStores';

import GameStore from '../stores/game';
import TitleActions from '../actions/title';

require('../styles/raw-output.less');

@connectToStores
class RawOutput extends Component {
  static getStores(props) {
    return [GameStore];
  }

  static getPropsFromStores(props) {
    const {game} = GameStore.getState();
    return {
      game
    };
  }

  componentWillMount() {
    TitleActions.setTitle('raw output');
  }

  render() {
    return (
      <div className="raw-output">
        <pre>
          {JSON.stringify(this.props.game, null, 2)}
        </pre>
      </div>
    );
  }
}

export default RawOutput;
