import axios from "axios";
import { GET_ACCOUNTS } from "./types";
import { tokenConfig } from "./auth";

//Get account
export const getAccounts = () => (dispatch, getState) => {
  axios
    .get("/api/paymentSum/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_ACCOUNTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
