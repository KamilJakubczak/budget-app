import axios from "axios";
import {
  GET_TRANSACTIONS,
  ADD_TRANSACTION,
  GET_ERRORS,
  DELETE_TRANSACTION,
} from "./types";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

//Get account
export const getTransactions = () => (dispatch, getState) => {
  axios
    .get("/api/transactions", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_TRANSACTIONS,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const addTransaction = (transaction) => (dispatch, getState) => {
  axios
    .post("/api/transactions/", transaction, tokenConfig(getState))
    .then((res) => {
      dispatch(
        createMessage({
          transactionAdded: "Transaction added",
        })
      );
      dispatch({
        type: ADD_TRANSACTION,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const deleteTransaction = (id) => (dispatch, getState) => {
  axios
    .delete(`/api/transactions/${id}/`, tokenConfig(getState))
    .then((res) => {
      dispatch(
        createMessage({
          transactionDeleted: "Transaction deleted",
        })
      );
      dispatch({
        type: DELETE_TRANSACTION,
        payload: res.data,
      });
    })
    .catch((err) => {
      const errors = {
        msg: err.response.data,
        status: err.response.status,
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors,
      });
    });
};
