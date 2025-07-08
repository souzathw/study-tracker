import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import { createPinia } from 'pinia'
import router from './router'
import axios from 'axios'

const app = createApp(App)

axios.defaults.baseURL = 'http://localhost:8000'
const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

app.use(createPinia())
app.use(router)
app.mount('#app')
