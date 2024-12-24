<template>
    <header class="relative min-h-screen flex flex-col items-center justify-center bg-gray-100 overflow-hidden">
      <!-- Section Title -->
      <h1 class="text-4xl font-extrabold text-green-700 mb-8 text-center">
        What FarmEye Can Do
      </h1>
  
      <!-- Features Section adding suitable images to the feature cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 px-6 max-w-7xl">
        <!-- Feature Card -->
        <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
          <div class="p-4 bg-green-100 rounded-full mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Crop Prediction</h3>
          <p class="text-gray-600 text-center">
            Get tailored crop suggestions based on your soil type and environmental factors.
          </p>
        </div>
  
        <!-- Feature Card -->
        <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
          <div class="p-4 bg-green-100 rounded-full mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Pests & Diseases Dictionary</h3>
          <p class="text-gray-600 text-center">
            Learn how to identify and treat common pests and diseases effectively.
          </p>
        </div>
  
        <!-- Feature Card -->
        <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
          <div class="p-4 bg-green-100 rounded-full mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4v2m-6-6h12" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Comprehensive Farming Guide</h3>
          <p class="text-gray-600 text-center">
            Access detailed guides on farming techniques, best practices, and more.
          </p>
        </div>
  
        <!-- Feature Card -->
        <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-md">
          <div class="p-4 bg-green-100 rounded-full mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7 7 7-7M13 5l7 7-7 7m0 0l-7-7" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Accurate Weather Prediction</h3>
          <p class="text-gray-600 text-center">
            Stay informed with precise weather updates to plan your farming activities.
          </p>
        </div>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: "Features",
  };
  </script>
  
  <style scoped>
  </style>
  