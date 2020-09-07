import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getAccounts } from "../../actions/accounts";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { withStyles } from "@material-ui/core/styles";
const useStyles = (theme) => ({
  grid: {
    flexGrow: 1,
    margin: theme.spacing(4),
  },
  root: {
    flexGrow: 1,
    display: "flex",
    flexWrap: "wrap",
    textAlign: "center",
    "& > *": {
      margin: theme.spacing(3),
      width: theme.spacing(16),
      height: theme.spacing(16),
    },
  },
});

export class Accounts extends Component {
  static propTypes = {
    accounts: PropTypes.array.isRequired,
    getAccounts: PropTypes.func.isRequired,
  };
  componentDidMount() {
    this.props.getAccounts();
  }
  render() {
    const { classes } = this.props;
    return (
      <Fragment>
        <Grid id="1" className={classes.grid} spacing={2}>
          <Grid id="2" item xs={12}>
            <Grid container justify="center" spacing={3}>
              {this.props.accounts.map((account) => (
                <Paper
                  key={account.name}
                  className={classes.root}
                  elevation={3}
                >
                  <span>
                    <h3>{account.name}</h3>
                    <p>{account.sum}</p>
                  </span>
                </Paper>
              ))}
            </Grid>
          </Grid>
        </Grid>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  accounts: state.accounts.accounts,
});
export default connect(mapStateToProps, { getAccounts })(
  withStyles(useStyles)(Accounts)
);
