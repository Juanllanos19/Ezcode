import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Particles from "vue3-particles"
import './assets/main.css'
import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000/api/"

const app = createApp(App).use(Particles);

app.config.errorHandler = (err) => {console.log(err)};

app.use(store)

app.use(router, axios)

app.mount('#app')

