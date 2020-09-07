import axios from "axios";
import {
  GET_TRANSACTIONS,
  ADD_TRANSACTION,
  GET_ERRORS,
  DELETE_TRANSACTION,
} from "./types";
import { createMessage } from "./messages";

//Get account
export const getTransactions = () => (dispatch) => {
  axios
    .get("/api/transactions")
    .then((res) => {
      dispatch({
        type: GET_TRANSACTIONS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};

export const addTransaction = (transaction) => (dispatch) => {
  axios
    .post("/api/transactions/", transaction)
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

export const deleteTransaction = (id) => (dispatch) => {
  axios
    .delete(`/api/transactions/${id}/`)
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
