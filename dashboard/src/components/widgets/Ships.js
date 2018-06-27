import React, { Component } from 'react';
import connectToStores from 'alt-utils/lib/connectToStores';

import GameStore from '../../stores/game';

import Widget from '../widget';

require('../../styles/widgets/ships.less');

@connectToStores
class Ships extends Component {
  static getStores(props) {
    return [GameStore];
  }

  static getPropsFromStores(props) {
    const ships = GameStore.getObjectsByType("simulation.ships.ship.Ship");
    return {
      ships
    };
  }

  state = {
    expanded: []
  };

  _toggleExpanded = (i) => {
    let expanded = this.state.expanded;
    if (expanded.indexOf(i) !== -1) {
      expanded.splice(expanded.indexOf(i), 1);
    } else {
      expanded.push(i);
    }

    this.setState({
      expanded
    });
  };

  render() {
    return (
      <Widget name="ships">
        <pre className="ships">
          {this.props.ships.map((ship, i) => {
            let destination = 'None';
            if(ship.destination) {
              destination = `${ship.destination.x}, ${ship.destination.y}`;
            }

            return <p key={`ship-${i}`}>Ship @ {ship.x.toFixed(0)} {ship.y.toFixed(0)}<br/>Destination: {destination}</p>
          })}
        </pre>
      </Widget>
    );
  }
}

export default Ships;