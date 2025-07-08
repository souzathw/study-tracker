<template>
    <div class="max-w-md mx-auto bg-white p-6 rounded shadow mt-10">
      <h2 class="text-2xl font-bold text-center mb-4">Sessão de Estudo / Pausa</h2>
  
      <div class="mb-4">
        <label class="block mb-1 font-medium">Minutos:</label>
        <input v-model.number="minutes" type="number" class="border w-full p-2" placeholder="Ex: 25" />
      </div>
  
      <div class="mb-4">
        <label class="block mb-1 font-medium">Tag (assunto):</label>
        <input v-model="tagName" type="text" class="border w-full p-2" placeholder="Ex: Matemática" />
      </div>
  
      <div class="mb-4">
        <label class="block mb-1 font-medium">Tipo:</label>
        <select v-model="type" class="border w-full p-2">
          <option value="study">Estudo</option>
          <option value="pause">Pausa</option>
        </select>
      </div>
  
      <div class="flex justify-between mb-4">
        <button @click="startTimer" :disabled="isRunning" class="bg-green-500 text-white px-4 py-2 rounded">
          Iniciar {{ type === 'study' ? 'Estudo' : 'Pausa' }}
        </button>
        <button @click="stopTimer" :disabled="!isRunning" class="bg-red-500 text-white px-4 py-2 rounded">
          Cancelar
        </button>
      </div>
  
      <div v-if="isRunning" class="text-center text-3xl font-bold text-blue-600">
        {{ display }}
      </div>
  
      <div class="mt-6 text-center">
        <button @click="finalizarDia" class="text-sm text-gray-600 underline">Finalizar Dia</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const minutes = ref(25)
  const tagName = ref('')
  const type = ref('study')
  const isRunning = ref(false)
  const display = ref('')
  let timer = null
  let startTime = null
  
  const startTimer = async () => {
    if (!tagName.value || !minutes.value) return alert('Preencha o tempo e a tag')
  
    isRunning.value = true
    startTime = new Date()
  
    let remaining = minutes.value * 60
    updateDisplay(remaining)
  
    timer = setInterval(() => {
      remaining--
      updateDisplay(remaining)
      if (remaining <= 0) {
        clearInterval(timer)
        isRunning.value = false
        playAlarm()
        salvarBloco()
      }
    }, 1000)
  }
  
  const stopTimer = () => {
    clearInterval(timer)
    isRunning.value = false
    display.value = ''
  }
  
  const updateDisplay = (seconds) => {
    const m = String(Math.floor(seconds / 60)).padStart(2, '0')
    const s = String(seconds % 60).padStart(2, '0')
    display.value = `${m}:${s}`
  }
  
  const playAlarm = () => {
    const audio = new Audio('/alarm.mp3')
    audio.play()
  }
  
  const salvarBloco = async () => {
    try {
      // 1. Garante que o dia existe
      const dia = await axios.post('/study/start-day')
      const study_day_id = dia.data.id
  
      // 2. Cria a tag se necessário
      const tagRes = await axios.post('/study/tag', {
        name: tagName.value,
        type: type.value
      })
      const tag_id = tagRes.data.id
  
      // 3. Cria o bloco
      const endTime = new Date()
      const diffMin = Math.round((endTime - startTime) / 60000)
  
      await axios.post('/study/block', {
        study_day_id,
        tag_id,
        start_time: startTime.toISOString(),
        end_time: endTime.toISOString(),
        duration_minutes: diffMin,
        type: type.value
      })
  
      alert('Bloco registrado com sucesso!')
    } catch (err) {
      console.error(err)
      alert('Erro ao salvar o bloco.')
    }
  }
  
  const finalizarDia = () => {
    alert('O dia foi finalizado! (ainda sem lógica de backend)')
  }
  </script>
  