<script lang="ts" setup>
import { ref } from 'vue'

const isLoggedIn = ref(false)

const handleLogin = () => {
  // Add your login logic here
  console.log('Login clicked')
}

const handleLogout = () => {
  isLoggedIn.value = false
  console.log('Logged out')
}
</script>

<template>
  <header class="bg-gray-800 border-b border-gray-700 shadow-lg">
    <div class="max-w-6xl mx-auto px-6 py-4">
      <div class="flex items-center justify-between">
        <!-- Title/Logo on the left -->
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-blue-400">
            TodoApp
          </h1>
        </div>

        <!-- Login/User section on the right -->
        <div class="flex items-center space-x-4">
          <div v-if="!isLoggedIn">
            <button
              @click="handleLogin"
              class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg transition-colors duration-200"
            >
              Login
            </button>
          </div>
          
          <div v-else class="flex items-center space-x-3">
            <span class="text-gray-300">Welcome, User!</span>
            <button
              @click="handleLogout"
              class="bg-gray-600 hover:bg-gray-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

