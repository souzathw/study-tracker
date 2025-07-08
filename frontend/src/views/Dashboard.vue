<template>
    <div class="max-w-4xl mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
  
      <div v-if="!user">Área privada acessível após login</div>
  
      <div v-else>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <canvas ref="dayChart"></canvas>
            <p class="text-center mt-2 font-semibold">Hoje</p>
          </div>
          <div>
            <canvas ref="weekChart"></canvas>
            <p class="text-center mt-2 font-semibold">Semana</p>
          </div>
          <div>
            <canvas ref="monthChart"></canvas>
            <p class="text-center mt-2 font-semibold">Mês</p>
          </div>
          <div>
            <canvas ref="tagsChart"></canvas>
            <p class="text-center mt-2 font-semibold">Top Tags</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useAuthStore } from '../stores/auth'
  import axios from 'axios'
  import Chart from 'chart.js/auto'
  
  const auth = useAuthStore()
  const user = computed(() => auth.user)
  
  const dayChart = ref(null)
  const weekChart = ref(null)
  const monthChart = ref(null)
  const tagsChart = ref(null)
  
  onMounted(async () => {
    if (!user.value) return
  
    const token = localStorage.getItem('token')
    const { data } = await axios.get('http://localhost:8000/dashboard', {
      headers: { Authorization: `Bearer ${token}` }
    })
  
    const formatData = (blocks) => {
      const study = blocks.find(b => b.type === 'Estudo')?.minutes || 0
      const pause = blocks.find(b => b.type === 'Pausa')?.minutes || 0
      return {
        labels: ['Estudo', 'Pausa'],
        datasets: [{ data: [study, pause], backgroundColor: ['#2563eb', '#fbbf24'] }]
      }
    }
  
    new Chart(dayChart.value, { type: 'doughnut', data: formatData(data.day) })
    new Chart(weekChart.value, { type: 'doughnut', data: formatData(data.week) })
    new Chart(monthChart.value, { type: 'doughnut', data: formatData(data.month) })
  
    const tagLabels = data.top_tags.map(t => `${t.name} (${t.type})`)
    const tagCounts = data.top_tags.map(t => t.count)
    new Chart(tagsChart.value, {
      type: 'bar',
      data: {
        labels: tagLabels,
        datasets: [{ data: tagCounts, label: 'Top Tags', backgroundColor: '#10b981' }]
      }
    })
  })
  </script>
  