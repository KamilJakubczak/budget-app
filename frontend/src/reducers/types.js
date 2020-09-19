import { GET_TYPES } from "../actions/types.js";

const initialState = {
  types: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_TYPES:
      return {
        ...state,
        types: action.payload,
      };
    default:
      return state;
  }
}
