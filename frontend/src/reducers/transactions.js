import { GET_TRANSACTIONS, ADD_TRANSACTION } from "../actions/types.js";

const initialState = {
  transactions: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_TRANSACTIONS:
      return {
        ...state,
        transactions: action.payload,
      };
    case ADD_TRANSACTION:
      return {
        ...state,
        transactions: [...state.transactions, action.payload],
      };
    default:
      return state;
  }
}
