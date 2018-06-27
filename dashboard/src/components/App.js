import React, { Component } from 'react';
import { Link } from 'react-router';

import Planets from './widgets/Planets';
import Ships from './widgets/Ships';
import Widget from './widget';

import connectToStores from 'alt-utils/lib/connectToStores';

import GameStore from '../stores/game';
import GameActions from '../actions/game';
import TitleStore from '../stores/title';

require('../styles/app.less');

@connectToStores
class App extends Component {
  static getStores(props) {
    return [GameStore, TitleStore];
  }

  static getPropsFromStores(props) {
    const {status} = GameStore.getState();
    const {title} = TitleStore.getState();
    return {
      status,
      title
    };
  }

  componentDidMount() {
    GameActions.connect();
  }

  render() {
    return (
      <div className="app">
        <section className="content">
          <header>
            <h4>{this.props.title}</h4>
            <div className="action-status">
              <Link to="/map">Map</Link>
              <Link to="/">Home</Link>
              |
              <a href="#" onClick={GameActions.start} title="Start Simulation"><i className="fa fa-play"></i></a>
              <a href="#" onClick={GameActions.stop} title="Pause Simulation"><i className="fa fa-pause"></i></a>
              <a href="#" onClick={GameActions.restart} title="Restart Simulation"><i className="fa fa-refresh"></i></a>
              <a href="#" onClick={GameActions.generate} title="Regenerate Universe"><i className="fa fa-balance-scale"></i></a>

              <h4>status: {this.props.status}</h4>
            </div>
          </header>

          <main role="content">
            {this.props.children}
          </main>

        </section>

        <section className="widgets">
          <Planets />
          <Ships />
          <Widget name="goods" />
        </section>
      </div>
    );
  }
}

export default App;
