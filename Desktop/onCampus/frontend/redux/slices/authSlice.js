import { createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

const initialState = {};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {},
});

export default authSlice.reducer;

export const registerUser =
    (username, email, password1, password2,router) =>
        async (dispatch) => {
            try {
                const url = '/api/auth/register/';
                await axios.post(url, { username, email, password1, password2 });
                router.push('/auth/login');
            } catch (error) {
                console.log(error);
            }
        };