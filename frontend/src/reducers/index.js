import { combineReducers } from "redux";
import accounts from "./accounts";
import transactions from "./transactions";
import types from "./types";
import categories from "./categories";
import tags from "./tags";
import payments from "./payments";

export default combineReducers({
  accounts,
  transactions,
  types,
  categories,
  tags,
  payments,
});
