<!--<template>
    <div>
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
                <label for="name" class="sr-only">Name</label>
                <input 
                  id="name" 
                  name="name" 
                  type="text" 
                  required 
                  class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                  placeholder="Name"
                  v-model="name"
                 />
                </div>
               <div>
              <label for="email" class="sr-only">Email address</label>
              <input 
                id="email" 
                name="email" 
                type="email" 
                required 
                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                placeholder="Email address"
                v-model="email"
              />
            </div>
            <div>
              <label for="text" class="sr-only">Name of Farm</label>
              <input 
                id="farmname" 
                name="farmname" 
                type="text" 
                required 
                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                placeholder="Name of farm"
                v-model="farmname"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input 
                id="password" 
                name="password" 
                type="password" 
                required 
                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                placeholder="Password"
                v-model="password"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input 
                id="password" 
                name="password" 
                type="password" 
                required 
                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" 
                placeholder="Confirm Password"
                v-model="password"
              />
            </div>
          </div>
          <div>
            <button 
              type="submit" 
              class="relative flex justify-center w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 border border-transparent rounded-md group hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Sign Up
            </button>
            <p class="m-4 text-gray-900">Already have an account? <router-link to="/signin" class="py-2 hover:text-blue-500 hover:underline">Login Instead</router-link> </p>
          </div>
        </form>
      </div>
    </div>
    </div>
   </div>
</template>-->


<template>
    <div>
      <img src="../assets/farming.webp" alt="farming image" class="image" />
      <div class="image_caption">
        <div class="flex items-center justify-center">
          <div class="w-full max-w-md p-8 space-y-8 bg-white rounded shadow-md">
            <div class="text-center">
              <h2 class="text-3xl font-extrabold text-green-700">Sign Up</h2>
            </div>
            <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
              <div class="rounded-md shadow-sm">
                <!-- Name -->
                <div>
                  <label for="name" class="sr-only">Name</label>
                  <input
                    id="name"
                    name="name"
                    type="text"
                    required
                    class="relative block w-full px-3 py-2 text-green-700 placeholder-green-500 border border-gray-300 rounded-t-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm"
                    placeholder="Name"
                    v-model="name"
                  />
                </div>
  
                <!-- Email -->
                <div>
                  <label for="email" class="sr-only">Email address</label>
                  <input
                    id="email"
                    name="email"
                    type="email"
                    required
                    class="relative block w-full px-3 py-2 text-green-700 placeholder-green-500 border border-gray-300 focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm"
                    placeholder="Email address"
                    v-model="email"
                  />
                </div>
  
                <!-- Name of Farm -->
                <div>
                  <label for="farmname" class="sr-only">Name of Farm</label>
                  <input
                    id="farmname"
                    name="farmname"
                    type="text"
                    required
                    class="relative block w-full px-3 py-2 text-green-700 placeholder-green-500 border border-gray-300 focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm"
                    placeholder="Name of Farm"
                    v-model="farmname"
                  />
                </div>
  
                <!-- Password -->
                <div>
                  <label for="password" class="sr-only">Password</label>
                  <input
                    id="password"
                    name="password"
                    type="password"
                    required
                    class="relative block w-full px-3 py-2 text-green-700 placeholder-green-500 border border-gray-300 focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm"
                    placeholder="Password"
                    v-model="password"
                  />
                </div>
  
                <!-- Confirm Password -->
                <div>
                  <label for="confirm-password" class="sr-only">Confirm Password</label>
                  <input
                    id="confirm-password"
                    name="confirm-password"
                    type="password"
                    required
                    class="relative block w-full px-3 py-2 text-green-700 placeholder-green-500 border border-gray-300 rounded-b-md focus:outline-none focus:ring-green-500 focus:border-green-500 focus:z-10 sm:text-sm"
                    placeholder="Confirm Password"
                    v-model="confirmPassword"
                  />
                </div>
              </div>
  
              <!-- Sign Up Button -->
              <div>
                <button
                  type="submit"
                  class="relative flex justify-center w-full px-4 py-2 text-sm font-medium text-white bg-green-700 border border-transparent rounded-md group hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                >
                  Sign Up
                </button>
                <p class="m-4 text-green-700">
                  Already have an account?
                  <router-link
                    to="/signin"
                    class="py-2 hover:text-green-500 hover:underline"
                  >
                    Login Instead
                  </router-link>
                </p>
              </div>
            </form>
          </div>
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