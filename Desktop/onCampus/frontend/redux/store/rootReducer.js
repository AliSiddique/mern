import { combineReducers } from "redux";
import authReducer from "../slices/authSlice";

export default function createRootReducer(history) {
  return combineReducers({
    auth:authReducer
  });
}