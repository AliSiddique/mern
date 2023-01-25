import {
    configureStore,
  } from '@reduxjs/toolkit';
  import {useDispatch, useSelector } from 'react-redux';
  import { createWrapper } from 'next-redux-wrapper';
  import createRootReducer from './rootReducer';
  
  const rootReducer = createRootReducer();
  
  
  export const configuredStore = (initialState) => {
    // Create Store
    const store = configureStore({
      reducer: rootReducer,
      preloadedState: initialState,
    });
    return store;
  };
  
  export const store = configuredStore();
  export const useAppDispatch = () => useDispatch();
  export const useAppSelector = useSelector;
  export const wrapper = createWrapper(configuredStore);
