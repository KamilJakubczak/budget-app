import axios from "axios";
import { GET_TYPES } from "./types";
import { tokenConfig } from "./auth";

//Get account
export const getTypes = () => (dispatch, getStatus) => {
  axios
    .get("/api/transaction-types", tokenConfig(getStatus))
    .then((res) => {
      dispatch({
        type: GET_TYPES,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
