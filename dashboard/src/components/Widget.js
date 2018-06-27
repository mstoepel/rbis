import React, { Component } from 'react';

require('../styles/widget.less');

class Widget extends Component {
  render() {
    return (
      <div className="widget">
        <h4>{this.props.name}</h4>
          <div className="widget-body">
            {this.props.children}
          </div>
      </div>
    );
  }
}

export default Widget;
