<template>
  <header class="relative h-screen flex flex-col justify-between overflow-hidden">

    <!-- Background image -->
    <div class="absolute inset-0 bg-cover bg-no-repeat" :style="{ backgroundImage: `url(../src/assets/farmland.webp)` }"></div>

    <!--Navbar-->
    <!-- Logo -->
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
      <!-- Menu items -->
      <!--<a href="#" class="block py-2">Profile</a>-->
      <router-link to="/" class="block py-2">Home</router-link>
      <!--<router-link to="/logout" class="block py-2">Logout</router-link>-->
    </div>
    </nav>
    <!--End of Nav-->

    <!-- Description box -->
    <div class="absolute bottom-0 left-0 flex flex-col justify-between p-4 w-full sm:w-1/2 md:w-1/3 lg:w-1/4">
      <!-- Description box content -->
      <div class="flex flex-col space-y-2">
        <h1 class="text-4xl font-bold DM-Sans text-white">Crop Yield Predictions For Nigerian Soil</h1>
        <div class="flex items-center space-x-2">
          <span class="text-white" >
            Making optimum crop yield predictions
          </span>
        </div>
        <button class="inline-flex items-center space-x-2 bg-blue-500 text-white px-2 py-1 rounded-md hover:bg-blue-700">
            <svg
  xmlns="http://www.w3.org/2000/svg"
  fill="none"
  viewBox="0 0 24 24"
  stroke="currentColor"
  class="w-5 h-5"
>
  <path
    stroke-linecap="round"
    stroke-linejoin="round"
    stroke-width="2"
    d="M10 20.242V3.758C10 3.34 10.336 3 10.75 3c.177 0 .348.059.492.168l10 8a.75.75 0 0 1 0 1.164l-10 8a.75.75 0 0 1-.742.008.75.75 0 0 1-.508-.726z"
  />
</svg>
          <span>Predict Now</span>
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

