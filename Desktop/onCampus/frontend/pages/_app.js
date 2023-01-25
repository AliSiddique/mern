import '../styles/globals.css'
import { wrapper } from '../redux/store/store';
import axios from 'axios';
if(typeof window !== 'undefined') {

if (window.location.origin === "http://localhost:3000") {
  axios.defaults.baseURL = "http://127.0.0.1:8000"; // development server address
} else {
  axios.defaults.baseURL = window.location.origin; // production serevr address
}
}
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}

export default wrapper.withRedux(MyApp);
