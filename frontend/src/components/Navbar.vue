<template>
  <nav class="bg-azul text-white p-4 flex justify-between items-center">
    <router-link to="/" class="font-bold text-lg">Study Tracker</router-link>
    <div class="space-x-4">
      <router-link v-if="!token" to="/login">Login</router-link>
      <router-link v-if="!token" to="/register">Cadastrar</router-link>
      <router-link v-if="token" to="/dashboard">Dashboard</router-link>
      <router-link v-if="token" to="/study">Estudo</router-link>
      <button v-if="token" @click="logout" class="ml-4 underline">Sair</button>
    </div>
  </nav>
</template>

<script setup>
import { useAuthStore } from '../stores/auth'
import { computed } from 'vue'

const auth = useAuthStore()
const token = computed(() => auth.token)

const logout = () => {
  auth.logout()
}
</script>
