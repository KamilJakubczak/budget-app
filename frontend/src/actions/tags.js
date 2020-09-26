import axios from "axios";
import { GET_TAGS } from "./types";
import { tokenConfig } from "./auth";

//Get account
export const getTags = () => (dispatch, getState) => {
  axios
    .get("/api/tags", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_TAGS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
