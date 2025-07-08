<template>
    <div class="min-h-screen bg-creme flex items-center justify-center">
      <div class="bg-white p-8 rounded shadow w-full max-w-md">
        <h2 class="text-2xl font-bold mb-4 text-center">Cadastro</h2>
        <input v-model="username" type="text" placeholder="Nome de usuário" class="border w-full p-2 mb-4" />
        <input v-model="email" type="email" placeholder="Email" class="border w-full p-2 mb-4" />
        <input v-model="password" type="password" placeholder="Senha" class="border w-full p-2 mb-4" />
        <button @click="register" class="w-full bg-azul text-white py-2 rounded">Cadastrar</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '../stores/auth'
  
  const username = ref('')
  const email = ref('')
  const password = ref('')
  const auth = useAuthStore()
  
  const register = () => {
    auth.register(username.value, email.value, password.value)
  }
  </script>
  