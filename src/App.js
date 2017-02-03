import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import data from './mockData/data'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          Kopish?
          {data.numbers.map((n) => (<button>{n}</button> ))}
        </p>
      </div>
    );
  }
}

export default App;
