import { combineReducers } from "redux";
import accounts from "./accounts";
import transactions from "./transactions";

export default combineReducers({
  accounts,
  transactions,
});
