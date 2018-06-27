import React from 'react';
import { render } from 'react-dom';
import { Router, Route, IndexRoute, Link, browserHistory } from 'react-router'

import App from './components/App';
import RawOutput from './components/RawOutput';
import SystemMap from './components/SystemMap';

import debug from 'debug';
if (process.env.NODE_ENV === 'development') {
  debug.enable('dev');
  debug('dev')('Starting app...');

  const cssFileName = 'styles.css';
  const originalCallback = window.webpackHotUpdate;

  window.webpackHotUpdate = function (...args) {
      const links = document.getElementsByTagName('link');
      for (var i = 0; i < links.length; i++) {
          const link = links[i];
          if (link.href.search(cssFileName) !== -1) {
              let linkHref = link.href;
              link.href = 'about:blank';
              link.href = linkHref;
              originalCallback(...args);
              return;
          }
      }
  }
}

// <Route path="*" component={NoMatch}/>

render((
  <Router history={browserHistory}>
    <Route path="/" component={App}>
      <Route path="map" component={SystemMap} />
      <IndexRoute component={RawOutput} />
    </Route>
  </Router>
), document.getElementById('root'));