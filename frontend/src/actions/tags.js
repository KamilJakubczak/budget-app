import axios from "axios";
import { GET_TAGS } from "./types";

//Get account
export const getTags = () => (dispatch) => {
  axios
    .get("/api/tags")
    .then((res) => {
      dispatch({
        type: GET_TAGS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(res));
};
