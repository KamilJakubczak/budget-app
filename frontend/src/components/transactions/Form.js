import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addTransaction } from "../../actions/transactions";
import { getTypes } from "../../actions/transaction_types";
import { getCategories } from "../../actions/categories";
import { getTags } from "../../actions/tags";
import { getPayments } from "../../actions/payments";

export class Form extends Component {
  state = {
    transaction_date: "",
    type: "",
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
    console.log(transaction);
    this.props.addTransaction(transaction);
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
        <h2>Add transaction</h2>
        <form onSubmit={this.onSubmit}>
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
              {/* <option selected disabled>
                {" "}
                Payment source
              </option> */}
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
    );
  }
}

const mapStateToProps = (state) => ({
  types: state.types.types,
  categories: state.categories.categories,
  tags: state.tags.tags,
  payments: state.payments.payments,
});
export default connect(mapStateToProps, {
  addTransaction,
  getTypes,
  getCategories,
  getTags,
  getPayments,
})(Form);
