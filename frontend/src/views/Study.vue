<template>
  <div class="max-w-md mx-auto mt-10 p-4 bg-white rounded shadow">
    <h2 class="text-xl font-bold mb-4">Novo Bloco</h2>

    <div class="mb-4">
      <label class="block font-medium">Tipo:</label>
      <select v-model="blockType" class="w-full p-2 border rounded">
        <option value="Estudo">Estudo</option>
        <option value="Pausa">Pausa</option>
      </select>
    </div>

    <div class="mb-4">
      <label class="block font-medium">Duração (minutos):</label>
      <input type="number" v-model.number="duration" class="w-full p-2 border rounded" min="1" />
    </div>

    <div class="mb-4">
      <label class="block font-medium">Tags (opcional):</label>
      <input type="text" v-model="tags" class="w-full p-2 border rounded" placeholder="ex: matemática, revisão" />
    </div>

    <button @click="addBlock" class="bg-green-600 text-white px-4 py-2 rounded mb-4">Adicionar Bloco</button>

    <div v-if="currentBlock" class="text-center">
      <h3 class="text-lg font-bold mb-2">Bloco atual: {{ currentBlock.type }}</h3>
      <p class="text-4xl font-mono">{{ timeLeft }}</p>

      <div class="flex justify-center gap-4 mt-4">
        <button @click="startTimer" :disabled="isRunning" class="bg-blue-600 text-white px-4 py-2 rounded">
          Iniciar
        </button>
        <button @click="resetTimer" class="bg-gray-500 text-white px-4 py-2 rounded">
          Resetar
        </button>
      </div>

      <div v-if="dayFinished" class="text-green-700 font-bold mt-4">
        ✅ O dia foi finalizado!
      </div>

      <button v-if="!dayFinished" @click="finalizarDia"
        class="mt-4 px-4 py-2 bg-red-600 text-white rounded font-bold">Finalizar Dia</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useAuthStore } from '../stores/auth'
import axios from 'axios'

const blocks = ref([])
const currentIndex = ref(0)
const isRunning = ref(false)
const timeLeft = ref('00:00')
const timer = ref(null)
const duration = ref(25)
const blockType = ref('Estudo')
const tags = ref('')
const dayFinished = ref(false)

const currentBlock = computed(() => blocks.value[currentIndex.value])

const updateTimer = () => {
  if (!currentBlock.value) return
  const totalSeconds = currentBlock.value.duration * 60
  const minutes = Math.floor(totalSeconds / 60)
  const seconds = totalSeconds % 60
  timeLeft.value = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
}

const playSound = () => {
  const audio = new Audio('/finish.mp3')
  audio.play().catch(e => console.error('Erro ao tocar o som:', e))
}

const handleTimerEnd = () => {
  playSound()
  currentIndex.value++
  if (currentIndex.value < blocks.value.length) {
    updateTimer()
    startTimer()
  }
  checkIfDayFinished()
}

const checkIfDayFinished = () => {
  if (currentIndex.value >= blocks.value.length) {
    dayFinished.value = true
    console.log('Dia finalizado!')
  }
}

const startTimer = () => {
  if (!currentBlock.value) return
  let totalSeconds = currentBlock.value.duration * 60
  isRunning.value = true

  timer.value = setInterval(() => {
    totalSeconds--
    const minutes = Math.floor(totalSeconds / 60)
    const seconds = totalSeconds % 60
    timeLeft.value = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`

    if (totalSeconds <= 0) {
      clearInterval(timer.value)
      isRunning.value = false
      handleTimerEnd()
    }
  }, 1000)
}

const resetTimer = () => {
  clearInterval(timer.value)
  isRunning.value = false
  updateTimer()
}

const addBlock = () => {
  blocks.value.push({
    type: blockType.value,
    duration: duration.value,
    tags: tags.value,
  })
  if (!currentBlock.value) updateTimer()
}

const finalizarDia = async () => {
  dayFinished.value = true
  console.log('Dia finalizado manualmente!')
}

watch(currentBlock, () => updateTimer())
</script>
