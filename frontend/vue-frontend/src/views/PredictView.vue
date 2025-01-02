<template>
    <div class="min-h-screen bg-gray-100 flex justify-center items-center">
      <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-6">
        <h1 class="text-2xl font-bold text-center mb-4">Crop Prediction</h1>
        <form @submit.prevent="handlePredict" class="space-y-4">
          <div v-for="(label, field) in inputFields" :key="field" class="flex flex-col">
            <label :for="field" class="mb-1 font-medium text-gray-700">{{ label }}</label>
            <input
              :id="field"
              v-model="form[field]"
              type="text"
              class="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600 transition"
          >
            Predict
          </button>
        </form>
        <div v-if="prediction !== null" class="mt-6 text-center">
          <h2 class="text-xl font-semibold">Prediction</h2>
          <p class="text-lg text-gray-700">{{ prediction }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          pH: "",
          Nitrogen: "",
          Potassium: "",
          Phosphorus: "",
          OC: "",
          Particles: "",
          Water_holding_content: "",
          Soil_type: "",
        },
        prediction: null,
        inputFields: {
          pH: "pH (pH)",
          Nitrogen: "Nitrogen",
          Potassium: "Potassium",
          Phosphorus: "Phosphorus",
          OC: "OC",
          Particles: "Particles",
          Water_holding_content: "Water Holding Content",
          Soil_type: "Soil Type",
        },
      };
    },
    methods: {
      async handlePredict() {
        try {
          const response = await fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.form),
          });
  
          if (!response.ok) {
            throw new Error("Failed to fetch prediction");
          }
  
          const data = await response.json();
          this.prediction = data.prediction;
        } catch (error) {
          console.error("Error fetching prediction:", error);
          alert("Error fetching prediction. Check console for details.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
  }
  </style>
  