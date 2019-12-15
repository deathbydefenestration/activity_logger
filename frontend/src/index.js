import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

// REMOVE THIS AFTER TESTING - THIS IS SO THE APP RUNS
const mockUser = {
    id: 127,
    name: 'Michael Jordan',
    athlete_id: 25
  }

ReactDOM.render(<App user={mockUser}/>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
