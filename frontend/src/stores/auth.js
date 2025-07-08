import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || ''
  }),
  actions: {
    async login(email, password) {
      try {
        const response = await axios.post('http://localhost:8000/auth/login', {
          email,
          password
        })
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
        router.push('/dashboard')
      } catch (error) {
        alert('Login inválido')
        console.error(error)
      }
    },
    async register(username, email, password) {
      try {
        const response = await axios.post('http://localhost:8000/auth/register', {
          username,
          email,
          password
        })
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
        router.push('/dashboard')
      } catch (error) {
        alert('Erro ao registrar')
        console.error(error)
      }
    },
    logout() {
      this.token = ''
      this.user = null
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
      router.push('/login')
    }
  }
})
