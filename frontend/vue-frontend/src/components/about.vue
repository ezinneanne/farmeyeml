<template>
  <section class="relative min-h-screen flex flex-col justify-between overflow-hidden container mx-auto px-4 py-8">
    <!-- Section Title -->
    <h1 class="text-4xl font-extrabold text-green-700 mb-8 text-center p-4">
      About FarmEye
    </h1>

    <!-- Content Wrapper -->
    <div class="flex flex-col-reverse md:flex-row items-center justify-between h-full gap-6">
      <!-- Text Content -->
      <div class="md:w-1/2 p-4 text-center md:text-left">
        <h2 class="text-2xl font-bold mb-4 text-green-600">Our Story</h2>
        <p class="text-gray-700 leading-relaxed">
          FarmEye is a farming productivity-oriented platform born out of a simple but pressing question: 
          How can we solve the countless problems facing Nigerian agriculture in a sustainable way?
        </p>
        <p class="text-gray-700 leading-relaxed mt-4">
          The idea for FarmEye emerged from observing the struggles of local farmers—low yields due to poor soil management, limited access to real-time data, and the absence of farmer-friendly technologies. Rather than focusing on quick fixes, we envisioned a platform that leverages smart policies, data-driven insights, and technology to transform the way farming is practiced.
        </p>
        <p class="text-gray-700 leading-relaxed mt-4">
          At its core, FarmEye aims to bridge the gap between traditional farming practices and modern agricultural innovation. By providing farmers with actionable insights, improved resource management, and decision-support tools, the platform helps boost productivity while ensuring sustainability. Our mission is not just to support individual farmers but to contribute to reshaping the broader agricultural landscape in Nigeria.
        </p>
      </div>

      <!-- Image Content -->
      <div class="md:w-1/2 p-4 flex justify-center">
        <img
          src="../assets/farmers.jpg"
          alt="FarmEye Image"
          class="w-full max-w-sm md:max-w-full h-auto rounded-lg shadow-lg object-cover"
        />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "About",
};
</script>

<style scoped>
</style>
