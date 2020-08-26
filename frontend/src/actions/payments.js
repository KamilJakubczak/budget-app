import axios from "axios";
import { GET_PAYMENTS } from "./types";

//Get account
export const getPayments = () => (dispatch) => {
  axios
    .get("/api/payment")
    .then((res) => {
      dispatch({
        type: GET_PAYMENTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
