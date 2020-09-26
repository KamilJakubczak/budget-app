import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
  };

  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;

    if (error.msg.non_field_errors) {
      alert.error(error.msg.non_field_errors.join());
      console.log(error.msg.non_field_errors.join());
    }
    if (error !== prevProps.error) {
      for (const e in error.msg) {
        alert.error(`${e.replace("_", " ")}`);
      }
    }

    if (message.passwordNotMatch) alert.error(message.passwordNotMatch);
    if (message !== prevProps.message) {
      alert.success(message.transactionAdded);
    }
  }

  render() {
    return <Fragment />;
  }
}
const mapStateToProps = (state) => ({
  error: state.errors,
  message: state.messages,
});

export default connect(mapStateToProps)(withAlert()(Alerts));
