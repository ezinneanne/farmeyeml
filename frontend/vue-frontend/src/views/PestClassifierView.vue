<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">Crop Disease Detector</h2>
    <input type="file" @change="onFileChange" class="mb-4" />
    <button @click="uploadImage" class="px-4 py-2 bg-blue-600 text-white rounded">
      Analyze
    </button>

    <div v-if="result" class="mt-6 p-4 border rounded bg-gray-100">
      <p><strong>Disease/Pest:</strong> {{ result.class }}</p>
      <p><strong>Confidence:</strong> {{ result.confidence }}</p>
      <p><strong>Treatment:</strong> {{ result.treatment }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const file = ref(null)
const result = ref(null)

function onFileChange(e) {
  file.value = e.target.files[0]
}

async function uploadImage() {
  if (!file.value) return
  const formData = new FormData()
  formData.append('file', file.value)

  const response = await fetch('http://127.0.0.1:8000/predict/', {
    method: 'POST',
    body: formData,
  })
  result.value = await response.json()
}
</script>
