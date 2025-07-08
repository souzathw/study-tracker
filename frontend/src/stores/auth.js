import { defineStore } from 'pinia'
import axios from 'axios'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || '')
  const user = ref(JSON.parse(localStorage.getItem('user')) || null)

  const login = async (credentials) => {
    const response = await axios.post('http://localhost:8000/auth/login', credentials)
    token.value = response.data.access_token
    user.value = response.data.user

    localStorage.setItem('token', response.data.access_token)
    localStorage.setItem('user', JSON.stringify(response.data.user))
  }

  const register = async (data) => {
    const response = await axios.post('http://localhost:8000/auth/register', data)
    token.value = response.data.access_token
    user.value = response.data.user

    localStorage.setItem('token', response.data.access_token)
    localStorage.setItem('user', JSON.stringify(response.data.user))
  }

  const logout = () => {
    token.value = ''
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  return { token, user, login, register, logout }
})