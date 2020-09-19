import axios from "axios";
import { GET_TYPES } from "./types";

//Get account
export const getTypes = () => (dispatch) => {
  axios
    .get("/api/transaction-types")
    .then((res) => {
      dispatch({
        type: GET_TYPES,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
