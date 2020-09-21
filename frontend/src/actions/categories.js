import axios from "axios";
import { GET_CATEGORIES } from "./types";
import { tokenConfig } from "./auth";

//Get account
export const getCategories = () => (dispatch, getState) => {
  axios
    .get("/api/categories", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_CATEGORIES,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
