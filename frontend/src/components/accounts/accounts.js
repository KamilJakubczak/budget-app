import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getAccounts } from "../../actions/accounts";

export class Accounts extends Component {
  static propTypes = {
    accounts: PropTypes.array.isRequired,
    getAccounts: PropTypes.func.isRequired,
  };
  componentDidMount() {
    this.props.getAccounts();
  }
  render() {
    return (
      <Fragment>
        <h2>Accounts:</h2>
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Account name</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            {this.props.accounts.map((account) => (
              <tr key={account.name}>
                <td>{account.name}</td>
                <td>{account.sum}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  accounts: state.accounts.accounts,
});
export default connect(mapStateToProps, { getAccounts })(Accounts);
