import axios from "axios";
import { GET_ACCOUNTS } from "./types";

//Get account
export const getAccounts = () => (dispatch) => {
  axios
    .get("/api/paymentSum")
    .then((res) => {
      dispatch({
        type: GET_ACCOUNTS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
