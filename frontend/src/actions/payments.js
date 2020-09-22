import axios from "axios";
import { GET_PAYMENTS } from "./types";
import { tokenConfig } from "./auth";

//Get account
export const getPayments = () => (dispatch, getState) => {
  axios
    .get("/api/payment", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_PAYMENTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
