import { GET_ACCOUNTS } from "../actions/types.js";

const initialState = {
  accounts: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_ACCOUNTS:
      return {
        ...state,
        accounts: action.payload,
      };
    default:
      return state;
  }
}
