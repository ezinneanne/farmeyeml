<template>
    <img src="../assets/farming.webp" alt="movie image" class="image"/>
    <div class="image_caption">
       <div class="flex items-center justify-center">
         <div class="w-full max-w-md p-8 space-y-8 bg-white rounded shadow-md">
         <div class="text-center">
           <h2 class="text-3xl font-extrabold text-green-700">Sign In</h2>
         </div>
         <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
           <div class="rounded-md shadow-sm">
             <div>
                <label for="email" class="sr-only">Email address</label>
                <input id="email" name="email" type="email" required class="relative block w-full px-3 py-2 text-green-700 placeholder-green-600 border border-gray-300 rounded-t-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm" 
  placeholder="Email address" v-model="email"/>
             <label for="password" class="sr-only">Password</label>
             <input 
               id="password" 
               name="password" 
               type="password" 
               required 
               class="relative block w-full px-3 py-2 text-green-700 placeholder-green-600 border border-gray-300 rounded-t-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm" 
               placeholder="Password"
               v-model="password"
             />
            </div>
         </div>
         <p v-if="errMsg">{{ errMsg }}</p>
         <div>
           <button 
             type="submit"
             @click="signIn" 
             class="relative flex justify-center w-full px-4 py-2 text-sm font-medium text-white bg-green-700 border border-transparent rounded-md group hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
           >
             Sign In
           </button>
           <p class="m-4 text-green-700">Don't have an account? <router-link to="/signup" class="py-2 hover:text-green-500 hover:underline">Register Instead</router-link></p>
         </div>
      </form>
    </div>
   </div>
  </div>
</template>
 

<script>

</script>

<style scoped>
.image {
  display: block;
  width: 100%;
  width: 100vw;
  height: 100vh;
  object-fit: cover;
}

.image_caption{
 position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: 3rem 4rem;
  text-align: center;
  color: #fff;
  z-index: 1;
}
</style>