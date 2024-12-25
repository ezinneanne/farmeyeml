<template>
    <footer class="bg-black text-white py-8">
      <section class="container mx-auto px-4">
        <div class="flex flex-wrap justify-between gap-14">
          <!-- Logo and About -->
          <div class="w-full md:w-1/3">
            <h1 class="text-2xl font-bold text-white mb-4">EZ Naturals.</h1>
            <p class="text-gray-400">
              EZ Naturals is a premier full-service beauty salon for women,
              conveniently situated in the heart of Lagos, Nigeria... 
              <a href="about.html" class="text-blue-500 font-semibold hover:text-white">Read More</a>
            </p>
          </div>
  
          <!-- Info Links -->
          <div class="w-full md:w-1/3">
            <h4 class="text-lg font-semibold mb-4">Info</h4>
            <ul class="space-y-2">
              <li><a href="index.html" class="hover:text-gray-400">Home</a></li>
              <li><a href="about.html" class="hover:text-gray-400">About</a></li>
              <li><a href="services.html" class="hover:text-gray-400">Services</a></li>
              <li><a href="lookbook.html" class="hover:text-gray-400">Lookbook</a></li>
              <li><a href="contact.html" class="hover:text-gray-400">Contact Us <i class="far fa-envelope"></i></a></li>
            </ul>
          </div>
  
          <!-- Newsletter -->
          <div class="w-full md:w-1/3">
            <h4 class="text-lg font-semibold mb-4">Newsletter</h4>
            <p class="text-gray-400 mb-4">
              Subscribe to our newsletter for a weekly dose of news, updates, healthy hair tips, and exclusive discounts.
            </p>
            <form class="flex gap-2">
              <input
                type="text"
                placeholder="Your email"
                required
                class="w-full px-4 py-2 border border-gray-400 rounded-md bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring focus:ring-gray-500"
              />
              <button
                type="submit"
                class="bg-white text-black px-4 py-2 rounded-md font-medium hover:bg-gray-400"
              >
                <a href="https://medium.com/@ezinneanne/subscribe">SUBSCRIBE</a>
              </button>
            </form>
            <div class="flex gap-4 mt-6">
              <a href="https://github.com/ezinneanne" class="hover:text-gray-400"><i class="fab fa-facebook fa-2x"></i></a>
              <a href="https://twitter.com/ezinne_anne" class="hover:text-gray-400"><i class="fab fa-instagram fa-2x"></i></a>
              <a href="https://twitter.com/ezinne_anne" class="hover:text-gray-400"><i class="fab fa-twitter fa-2x"></i></a>
            </div>
          </div>
        </div>
      </section>
      <hr class="border-gray-700 my-4" />
      <p class="text-center text-gray-500">Copyright &copy; 2024. All rights reserved</p>
    </footer>
  </template>
  

<script>
export default {
    name: "Footer",
  };
</script>