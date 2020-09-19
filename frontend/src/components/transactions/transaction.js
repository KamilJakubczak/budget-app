import React, { Component, Fragment } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTransactions, deleteTransaction } from "../../actions/transactions";
import Accounts from "../accounts/accounts";
import Form from "./Form";

export class Transactions extends Component {
  static propTypes = {
    transactions: PropTypes.array.isRequired,
    getTransactions: PropTypes.func.isRequired,
    deleteTransaction: PropTypes.func.isRequired,
  };
  componentDidMount() {
    this.props.getTransactions();
  }
  render() {
    return (
      <Fragment>
        <Accounts />
        <Form />
        <h2>Transactions:</h2>
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="row">ID</th>
              <th>Date</th>
              <th>Type</th>
              <th>Category</th>
              <th>Tag</th>
              <th>Description</th>
              <th>Amount</th>
              <th>Target</th>
              <th>Source</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.transactions.map((transaction) => (
              <tr key={transaction.id}>
                <td scope="row">{transaction.id}</td>
                <td>{transaction.transaction_date}</td>
                <td>{transaction.transaction_type}</td>
                <td>{transaction.category}</td>
                <td>{transaction.tag ? transaction.tag : "-"}</td>
                <td>{transaction.description}</td>
                <td>{transaction.amount}</td>

                <td>
                  {transaction.payment_target
                    ? transaction.payment_target
                    : "-"}
                </td>
                <td>
                  {transaction.payment_source
                    ? transaction.payment_source
                    : "-"}
                </td>
                <td>
                  <button
                    onClick={this.props.deleteTransaction.bind(this, transaction.id)}
                    className="btn btn-danger btn-sm"
                  >Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  transactions: state.transactions.transactions,
});
export default connect(mapStateToProps, { getTransactions, deleteTransaction })(Transactions);
