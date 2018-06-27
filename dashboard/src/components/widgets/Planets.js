import React, { Component } from 'react';
import connectToStores from 'alt-utils/lib/connectToStores';

import GameStore from '../../stores/game';

import Widget from '../widget';

require('../../styles/widgets/planets.less');

@connectToStores
class Planets extends Component {
  static getStores(props) {
    return [GameStore];
  }

  static getPropsFromStores(props) {
    let planets = [];

    const systems = GameStore.getObjectsByType("simulation.systems.system.SolarSystem");

    systems.map((system) => {
      planets = planets.concat(system.planets);
    });

    return {
      planets
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
      <Widget name="planets">
        <pre className="planets">
          {this.props.planets.map((planet, i) => {
            let moreData;
            if(this.state.expanded.indexOf(i) !== -1) {
              moreData = (
                <div className="more-data">
                  Population: {planet.pop} <br/>
                  Wealth: {planet.wealth}
                </div>
              )
            }

            return (
              <div className="planet" key={`planet-${i}`} onMouseEnter={() => this._toggleExpanded(i)} onMouseLeave={() => this._toggleExpanded(i)}>
                <i className="fa fa-globe"></i> <strong>Planet at {planet.x}, {planet.y}</strong> <br/>
                {moreData}
              </div>
            )
          })}
        </pre>
      </Widget>
    );
  }
}

export default Planets;