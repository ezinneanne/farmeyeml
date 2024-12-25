<template>
  <section class="bg-gray-100">
  <section class="relative h-screen flex flex-col justify-between overflow-hidden container mx-auto px-4">
    <h1 class="text-4xl font-extrabold text-green-700 mb-8 text-center p-4">
      Get In Touch
    </h1>
    <div class="flex flex-col md:flex-row items-center justify-center h-full">
      <div class="md:w-1/2 p-4 text-center md:text-left">
        <p class="text-gray-700 leading-relaxed">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
      </div>
      <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md mx-auto">
          <h3 class="text-2xl font-semibold mb-6 text-gray-800">Fill the form below:</h3>
          <form name="contact-form" method="post" data-netlify="true">
            <div class="mb-4">
              <label for="name" class="block text-gray-700 font-medium mb-2">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                placeholder="Enter your name here"
                required
                class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-green-300"
              />
            </div>
            <div class="mb-4">
              <label for="email" class="block text-gray-700 font-medium mb-2">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                placeholder="Enter your email here"
                required
                class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-green-300"
              />
            </div>
            <div class="mb-6">
              <label for="message" class="block text-gray-700 font-medium mb-2">Message</label>
              <textarea
                id="message"
                name="message"
                placeholder="Write your message here."
                class="w-full px-4 py-2 border rounded-md h-32 resize-y focus:outline-none focus:ring focus:ring-green-300"
              ></textarea>
            </div>
            <button type="submit" class="w-full bg-green-700 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring focus:ring-green-300">
              Submit
            </button>
          </form>
        </div>
      </div>
  </section>
  </section>
</template>

<script>
  export default {
    name: "Contact",
  };
  </script>