<template>
    <footer class="text-green-700 py-8">
      <section class="container mx-auto px-4">
        <div class="flex flex-wrap justify-between">
          <!-- Logo and About -->
          <div class="w-full md:w-1/3">
            <h1 class="text-2xl font-bold text-green-700 mb-4">FarmEye</h1>
            <p class="text-green-600">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
                Nesciunt reiciendis maiores dignissimos iste 
                optio officiis exercitationem quaerat velit alias.
            </p>
          </div>
  
          <!-- Info Links -->
          <div class="w-full md:w-1/3">
            <h4 class="text-2xl font-bold my-4">Info</h4>
            <ul class="space-y-2">
              <li><router-link to="/" class="hover:text-green-400">Home</router-link></li>
              <li><router-link to="/predict" class="hover:text-green-400">Crop Prediction</router-link></li>
              <li><a href="https://farmeyemldocs.netlify.app/" rel="noopener noreferrer" target="_blank" class="hover:text-green-400">Farming Guide</a></li>
              <li><router-link to="/weather" class="hover:text-green-400">Weather Forecast</router-link></li>
            </ul>
          </div>
  
          <!-- Newsletter -->
          <div class="w-full md:w-1/3">
            <h4 class="text-2xl font-bold my-4">Newsletter</h4>
            <p class="text-green-600 mb-4">
              Subscribe to our newsletter for a weekly dose of news, updates, important farming tips, and exclusive access to our advanced tech products.
            </p>
            <form class="flex gap-2">
              <input
                type="text"
                placeholder="Your email"
                required
                class="w-full px-4 py-2 border border-green-400 rounded-md bg-transparent text-white placeholder-green-400 focus:outline-none focus:ring focus:ring-green-500"
              />
              <button
                type="submit"
                class="bg-green-700 text-white px-4 py-2 rounded-md font-medium hover:bg-green-400"
              >
                <a href="https://medium.com/@ezinneanne/subscribe">SUBSCRIBE</a>
              </button>
            </form>
            <div class="flex gap-4 mt-6">
              <a href="https://github.com/ezinneanne" class="hover:text-green-400"><i class="fab fa-facebook fa-2x"></i></a>
              <a href="https://twitter.com/ezinne_anne" class="hover:text-green-400"><i class="fab fa-instagram fa-2x"></i></a>
              <a href="https://twitter.com/ezinne_anne" class="hover:text-green-400"><i class="fab fa-twitter fa-2x"></i></a>
            </div>
          </div>
        </div>
      </section>
      <hr class="border-green-700 my-4" />
      <p class="text-center text-green-600">Copyright &copy; {{ new Date().getFullYear() }}. All rights reserved</p>
    </footer>
  </template>
  

<script>
export default {
    name: "Footer",
  };
</script>