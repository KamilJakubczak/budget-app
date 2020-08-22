import React, { Component } from "react";
import React from "react-dom";

class App extends Component {
  render() {
    return <h1>React app</h1>;
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
