<script setup>
import { ref } from 'vue'
import Footer from '../components/footer.vue'

// reactive state
const file = ref(null)
const result = ref(null)

// handle file change
function onFileChange(e) {
  file.value = e.target.files[0]
}

// send image to FastAPI backend
async function uploadImage() {
  if (!file.value) return
  const formData = new FormData()
  formData.append('file', file.value)

  try {
    const response = await fetch('http://127.0.0.1:8000/predict/', {
      method: 'POST',
      body: formData,
    })
    result.value = await response.json()
  } catch (error) {
    console.error('Upload failed:', error)
  }
}
</script>

<template>
  <div class="p-6">
    <!-- File upload -->
    <input type="file" @change="onFileChange" class="mb-4" />
    <button 
      @click="uploadImage" 
      class="bg-blue-600 text-white px-4 py-2 rounded"
    >
      Upload & Predict
    </button>

    <!-- Show result -->
    <div v-if="result" class="mt-4 p-4 bg-gray-100 rounded">
      <pre>{{ result }}</pre>
    </div>

    <Footer />
  </div>
</template>
