import React, { Component } from 'react';
import connectToStores from 'alt-utils/lib/connectToStores';
import {Layer, Circle, Stage, Star} from 'react-konva';

import GameStore from '../stores/game';
import TitleActions from '../actions/title';

require('../styles/system-map.less');

@connectToStores
class SystemMap extends Component {
  static getStores(props) {
    return [GameStore];
  }

  static getPropsFromStores(props) {
    const systems = GameStore.getObjectsByType("simulation.systems.system.SolarSystem");

    return {
      systems,
    };
  }

  state = {
    system: 0
  };

  componentWillMount() {
    TitleActions.setTitle('system map');
  }

  render() {
    if(!this.props.systems || !this.props.systems.length) {
      return (
        <div className="system-map">
          <div className="no-system">
            No systems in game.
          </div>
        </div>
      )
    }

    const system = this.props.systems[this.state.system];

    return (
      <div className="system-map">
        <Stage width={884} height={478}>
          <Layer>
            <Circle x={442} y={239} radius={40} fill="#00ffff" shadowBlur={10} />
            {system.planets.map((planet, i) => {
              return (
                <Circle x={planet.x + 442} y={planet.y + 239} radius={15} key={`planet-${i}`} fill="#000000" shadowBlur={5} />
              );
            })}
            {system.ships.map((ship, i) => {
              return (
                <Star x={ship.x + 442} y={ship.y + 239} innerRadius={5} outerRadius={7} numPoints={3} key={`ship-${i}`} fill="#000000" />
              );
            })}
          </Layer>
        </Stage>
      </div>
    );
  }
}

export default SystemMap;
