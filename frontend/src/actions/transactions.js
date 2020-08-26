import axios from "axios";
import { GET_TRANSACTIONS, ADD_TRANSACTION } from "./types";

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

export const addTransaction = (transaction) => (dispatch, getState) => {
  axios
    .post("/api/transactions/", transaction)
    .then((res) => {
      dispatch({
        type: ADD_TRANSACTION,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
