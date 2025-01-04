<template>
  <header class="relative h-screen flex flex-col justify-between overflow-hidden">

    <!-- Background image -->
    <div class="absolute inset-0 bg-cover bg-no-repeat" :style="{ backgroundImage: `url(../src/assets/farmland.webp)` }"></div>

    <!-- Navbar -->
    <nav class="relative text-white flex justify-between items-center px-4 py-2 z-10">
      <div class="flex items-center text-white">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 mr-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        <span class="text-lg font-semibold">FarmEye</span>
      </div>

      <!-- Sign In -->
      <div class="flex items-center text-white">
        <router-link to="/signin" class="mr-2"> Sign in </router-link>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 cursor-pointer"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          @click="toggleMenu"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          />
        </svg>
      </div>

      <!-- Menu -->
      <div v-show="isMenuOpen" class="absolute top-full right-0 bg-gray-800 text-white mt-1 py-2 px-4 rounded shadow-lg">
        <router-link to="/" class="block py-2">Features</router-link>
        <router-link to="/" class="block py-2">About</router-link>
        <router-link to="/" class="block py-2">Contact</router-link> 
      </div>
    </nav>
    <!-- End of Navbar -->

    <!-- Description box -->
    <div class="absolute inset-0 flex items-center justify-center">
      <div class="flex flex-col items-center space-y-4 p-4 bg-opacity-50">
        <!-- Description box content -->
        <h1 class="text-4xl font-bold DM-Sans text-gray-600 text-center">
          High Productivity For Nigerian Soil
        </h1>
        <span class="font-bold text-gray-600 text-center">
          Improving productivity in Nigerian farms
        </span>
        <button class="inline-flex justify-center items-center bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-500">
          <router-link to="/predict" class="hover:underline">Predict Now</router-link>
        </button>
      </div>
    </div>
  </header>
</template>


<script>

export default {
  name: 'Header',

  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },

};
</script>

<style scoped>
/* Add Tailwind CSS classes as needed */
.DM-Sans {
  font-family: 'DM Sans', sans-serif;
}

</style>

