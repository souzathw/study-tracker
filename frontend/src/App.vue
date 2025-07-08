<template>
  <div class="min-h-screen bg-creme">
    <Navbar />
    <main class="p-4">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
</script>

<style>

</style>
