import { GET_PAYMENTS } from "../actions/types.js";

const initialState = {
  payments: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_PAYMENTS:
      return {
        ...state,
        payments: action.payload,
      };
    default:
      return state;
  }
}
