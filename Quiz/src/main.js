import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Particles from "vue3-particles";
import './assets/main.css'

const app = createApp(App).use(Particles);

app.config.errorHandler = (err) => {console.log(err)};

app.use(router)

app.mount('#app')
