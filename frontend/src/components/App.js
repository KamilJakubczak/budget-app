import React, {Component, Fragment} from "react";
import ReactDOM from "react-dom";
import {Provider as AlertProvider} from "react-alert";
import AlertTemplate from "react-alert-template-basic";
import Alerts from "./layout/Alerts";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
import Header from "./layout/Header";
import Accounts from "./accounts/accounts";
import Transactions from "./transactions/transaction";

import {Provider} from "react-redux";
import store from "../store";

//Alert options
const alertOptions = {
  timeout: 3000,
  position: 'top center'
}

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Router>
            <Fragment>
              <Header/>
              <Alerts/>
              <div className="container">
                <Switch>
                  <Route exact path="/accounts" component={Accounts}/>
                  <Route exact path="/transactions" component={Transactions}/>
                </Switch>
              </div>
            </Fragment>
          </Router>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById("app"));
