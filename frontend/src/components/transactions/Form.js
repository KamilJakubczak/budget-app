import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addTransaction } from "../../actions/transactions";
import { getTypes } from "../../actions/transaction_types";
import { getCategories } from "../../actions/categories";
import { getTags } from "../../actions/tags";
import { getPayments } from "../../actions/payments";
import { getAccounts } from "../../actions/accounts";

export class Form extends Component {
  state = {
    transaction_date: "",
    transaction_type: "",
    category: "",
    tag: "",
    description: "",
    amount: "",
    payment_target: "",
    payment_source: "",
  };

  static propTypes = {
    addTransaction: PropTypes.func.isRequired,
    types: PropTypes.array.isRequired,
    categories: PropTypes.array.isRequired,
    tags: PropTypes.array.isRequired,
    payments: PropTypes.array.isRequired,
    getTypes: PropTypes.func.isRequired,
    getCategories: PropTypes.func.isRequired,
    getTags: PropTypes.func.isRequired,
    getPayments: PropTypes.func.isRequired,
    getAccounts: PropTypes.func.isRequired,
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();

    const {
      transaction_date,
      transaction_type,
      category,
      tag,
      description,
      amount,
      payment_target,
      payment_source,
    } = this.state;

    const transaction = {
      transaction_date,
      transaction_type,
      category,
      tag,
      description,
      amount,
      payment_target,
      payment_source,
    };

    this.props.addTransaction(transaction);
    this.props.getAccounts();

    this.setState({
      transaction_date: "",
      transaction_type: "",
      category: "",
      tag: "",
      description: "",
      amount: "",
      payment_target: "",
      payment_source: "",
    });
  };

  componentDidMount() {
    this.props.getTypes();
    this.props.getCategories();
    this.props.getTags();
    this.props.getPayments();
    this.props.getAccounts();
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.categories.length !== 0 && this.state.category == "") {
      this.setState({ category: this.props.categories[0].id });
    }

    if (this.props.types.length !== 0 && this.state.transaction_type == "") {
      this.setState({ transaction_type: this.props.types[0].id });
    }
    console.log(this.props.categories);
  }

  render() {
    const {
      transaction_date,
      transaction_type,
      category,
      tag,
      description,
      amount,
      payment_target,
      payment_source,
    } = this.state;

    return (
      <div className=" card card-body mt-4 mb-4">
        <h2>
          <a
            className="btn btn-primary"
            data-toggle="collapse"
            href="#collapseTransactions"
            role="button"
          >
            Add transaction
          </a>
        </h2>
        <div className="collapse" id="collapseTransactions">
          <form onSubmit={this.onSubmit}>
            {/* Date */}
            <div className="form-group">
              <label>Date</label>
              <input
                className="form-control"
                type="date"
                name="transaction_date"
                onChange={this.onChange}
                value={transaction_date}
              />
            </div>

            {/* Transactin type */}
            <div className="form-group">
              <label>Transaction type</label>
              <select
                className="form-control"
                type="text"
                name="transaction_type"
                onChange={this.onChange}
                value={transaction_type}
              >
                {this.props.types.map((transaction_type) => (
                  <option key={transaction_type.id} value={transaction_type.id}>
                    {transaction_type.transaction_type}
                  </option>
                ))}
              </select>
            </div>
            {/* Category */}
            <div className="form-group">
              <label>Category</label>
              <select
                className="form-control"
                type="text"
                name="category"
                onChange={this.onChange}
                value={category}
              >
                {this.props.categories.map((category) => (
                  <option key={category.id} value={category.id}>
                    {category.name}
                  </option>
                ))}
              </select>
            </div>
            {/* Tag */}
            <div className="form-group">
              <label>Tag</label>
              <select
                className="form-control"
                type="text"
                name="tag"
                onChange={this.onChange}
                value={tag}
              >
                {this.props.tags.map((tag) => (
                  <option key={tag.id} value={tag.id}>
                    {tag.name}
                  </option>
                ))}
              </select>
            </div>
            {/* Desription */}
            <div className="form-group">
              <label>Description</label>
              <input
                className="form-control"
                type="text"
                name="description"
                onChange={this.onChange}
                value={description}
              />
            </div>
            <div className="form-group">
              <label>Amount</label>
              <input
                className="form-control"
                type="number"
                name="amount"
                onChange={this.onChange}
                value={amount}
              />
            </div>
            <div className="form-group">
              <label>Payment target</label>
              <select
                className="form-control"
                type="text"
                name="payment_target"
                onChange={this.onChange}
                value={payment_target}
              >
                {this.props.payments.map((payment_target) => (
                  <option key={payment_target.id} value={payment_target.id}>
                    {payment_target.payment}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <label>Payment source</label>
              <select
                className="form-control"
                type="text"
                name="payment_source"
                onChange={this.onChange}
                value={payment_source.id}
                placeholder="Payment source"
              >
                {this.props.payments.map((payment_source) => (
                  <option key={payment_source.id} value={payment_source.id}>
                    {payment_source.payment}
                  </option>
                ))}
              </select>
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
            {/*  */}
          </form>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  types: state.types.types,
  categories: state.categories.categories,
  tags: state.tags.tags,
  payments: state.payments.payments,
  accounts: state.accounts.accounts,
});

export default connect(mapStateToProps, {
  addTransaction,
  getTypes,
  getCategories,
  getTags,
  getPayments,
  getAccounts,
})(Form);
