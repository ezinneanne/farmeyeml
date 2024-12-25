<template>
  <section class="bg-gray-100">
    <section class="relative min-h-screen flex flex-col items-center justify-center overflow-hidden container mx-auto px-4">
      <!-- Section Title -->
      <h1 class="text-4xl font-extrabold text-green-700 mb-8 text-center">
        What FarmEye Can Do
      </h1>


      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-6 max-w-7xl">
  <!-- Feature Card -->
  <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
    <!-- Image -->
    <div class="p-4 mb-4">
      <img src="../assets/farmer.webp" alt="Crop Prediction" class="h-30 w-60 object-cover" />
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">Crop Prediction</h3>
    <p class="text-gray-600 text-center">
      Get tailored crop suggestions based on your soil type and environmental factors.
    </p>
  </div>

  <!-- Feature Card -->
  <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
    <!-- Image -->
    <div class="p-4 mb-4">
        <img src="../assets/pest.png" alt="Crop Prediction" class="h-30 w-60 object-cover" />
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">Pests & Diseases Dictionary</h3>
    <p class="text-gray-600 text-center">
      Learn how to identify and treat common pests and diseases effectively.
    </p>
  </div>

  <!-- Feature Card -->
  <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
    <!-- Image -->
    <div class="p-4 mb-4">
      <img src="../assets/farmguide.png" alt="Comprehensive Farming Guide" class="h-30 w-60 object-cover" />
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">Comprehensive Farming Guide</h3>
    <p class="text-gray-600 text-center">
      Access detailed guides on farming techniques, best practices, and more.
    </p>
  </div>

  <!-- Feature Card -->
  <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
    <!-- Image -->
    <div class="p-4 mb-4">
      <img src="../assets/weather.png" alt="Accurate Weather Prediction" class="h-30 w-60 object-cover" />
    </div>
    <h3 class="text-xl font-semibold text-gray-800 mb-2">Accurate Weather Prediction</h3>
    <p class="text-gray-600 text-center">
      Stay informed with precise weather updates to plan your farming activities.
    </p>
  </div>
</div>
      
</section>
</section>
  </template>
  
  <script>
  export default {
    name: "Features",
  };
  </script>
  
  <style scoped>
  </style>
  