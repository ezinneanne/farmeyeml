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
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p class="text-gray-700 leading-relaxed mt-4">
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
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
