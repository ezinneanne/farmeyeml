<template>
  <div class="min-h-screen flex justify-center items-center relative">

    <!-- Background image -->
    <div 
      class="absolute inset-0 bg-cover bg-no-repeat -z-10"
      :style="{ backgroundImage: `url(../src/assets/background.jpg)` }"
    ></div>

    <!-- Form container -->
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-6 relative z-10">
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
  <Footer />
</template>


<script>
import axios from "axios";
import Footer from '../components/footer.vue';
export default {
  components: {
    Footer,
  },
  data() {
    return {
      form: {
        pH: "",
        N: "",
        P: "",
        K: "",
        OC: "",
        Particles: "",
        Water_holding_content: "",
        Soil_type: "",
      },
      prediction: null,
      inputFields: {
        pH: "pH",
        N: "Nitrogen",
        P: "Phosphorus",
        K: "Potassium",
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
        const response = await axios.post("http://localhost:5000/predict", this.form, {
          headers: { "Content-Type": "application/json" },
        });

        this.prediction = response.data.prediction;
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
