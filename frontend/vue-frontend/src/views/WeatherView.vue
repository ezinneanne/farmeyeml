<template>
    <div class="flex flex-col items-center bg-gray-100 p-6 rounded-lg shadow-lg">
      <h1 class="text-2xl font-bold text-gray-800 mb-4">Weather Forecast</h1>
      <div class="flex items-center space-x-4 mb-6">
        <input
          type="text"
          v-model="state"
          placeholder="Enter your state"
          class="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-green-500"
        />
        <button
          @click="fetchWeather"
          class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
        >
          Get Weather
        </button>
      </div>
      <div v-if="weatherData" class="text-center">
        <p class="text-lg font-semibold text-gray-700">
          <span class="font-bold">Location:</span> {{ weatherData.city }}, {{ weatherData.country }}
        </p>
        <p class="text-lg font-semibold text-gray-700">
          <span class="font-bold">Temperature:</span> {{ weatherData.temperature }}°C
        </p>
        <p class="text-lg font-semibold text-gray-700">
          <span class="font-bold">Weather:</span> {{ weatherData.description }}
        </p>
      </div>
      <p v-else-if="errorMessage" class="text-red-500 font-semibold mt-4">
        {{ errorMessage }}
      </p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        state: "",
        weatherData: null,
        errorMessage: null,
      };
    },
    methods: {
      async fetchWeather() {
        if (!this.state.trim()) {
          this.errorMessage = "Please enter a state name.";
          this.weatherData = null;
          return;
        }
  
        const apiKey = ""; 
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${this.state.trim()}&appid=${apiKey}&units=metric`;
  
        try {
          const response = await fetch(apiUrl);
  
          if (!response.ok) {
            throw new Error("Unable to fetch weather data. Please check the state name.");
          }
  
          const data = await response.json();
          this.weatherData = {
            city: data.name,
            country: data.sys.country,
            temperature: data.main.temp,
            description: data.weather[0].description,
          };
          this.errorMessage = null;
        } catch (error) {
          this.errorMessage = error.message;
          this.weatherData = null;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  
  </style>
  