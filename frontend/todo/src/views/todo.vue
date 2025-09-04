


<script lang="ts" setup>
import { ref, computed } from 'vue'

interface Todo {
  id: number
  title: string
  description: string
  completed: boolean
}

const todos = ref<Todo[]>([])



const newTodoTitle = ref('')
const newTodoDescription = ref('')
const nextId = ref(3)

const activeTodos = computed(() => todos.value.filter(todo => !todo.completed))
const completedTodos = computed(() => todos.value.filter(todo => todo.completed))

const addTodo = () => {
  if (newTodoTitle.value.trim()) {
    todos.value.push({
      id: nextId.value++,
      title: newTodoTitle.value.trim(),
      description: newTodoDescription.value.trim(),
      completed: false
    })
    newTodoTitle.value = ''
    newTodoDescription.value = ''
  }
}

const toggleTodo = (id: number) => {
  const todo = todos.value.find(t => t.id === id)
  if (todo) {
    todo.completed = !todo.completed
  }
}

const deleteTodo = (id: number) => {
  const index = todos.value.findIndex(t => t.id === id)
  if (index > -1) {
    todos.value.splice(index, 1)
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-900 text-white p-6">
    <div class="max-w-4xl mx-auto">
      <!-- Add New Todo Form -->
      <div class="bg-gray-800 rounded-lg p-6 mb-8 shadow-lg">
        <h2 class="text-xl font-semibold mb-4 text-green-400">Add New Task</h2>
        <form @submit.prevent="addTodo" class="space-y-4">
          <div>
            <input
              v-model="newTodoTitle"
              type="text"
              placeholder="Task title..."
              class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-white placeholder-gray-400"
              required
            />
          </div>
          <div>
            <textarea
              v-model="newTodoDescription"
              placeholder="Task description (optional)..."
              rows="2"
              class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-white placeholder-gray-400 resize-none"
            ></textarea>
          </div>
          <button
            type="submit"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200"
          >
            Add Task
          </button>
        </form>
      </div>

      <div class="grid md:grid-cols-2 gap-8">
        <!-- Active Todos -->
        <div class="bg-gray-800 rounded-lg p-6 shadow-lg">
          <h2 class="text-2xl font-semibold mb-4 text-yellow-400">
            Active Tasks ({{ activeTodos.length }})
          </h2>
          <div v-if="activeTodos.length === 0" class="text-gray-400 text-center py-8">
            No active tasks. Great job! 🎉
          </div>
          <div v-else class="space-y-3">
            <div
              v-for="todo in activeTodos"
              :key="todo.id"
              class="bg-gray-700 rounded-lg p-4 border-l-4 border-yellow-400"
            >
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <h3 class="font-medium text-white">{{ todo.title }}</h3>
                  <p v-if="todo.description" class="text-gray-300 text-sm mt-1">
                    {{ todo.description }}
                  </p>
                </div>
                <div class="flex space-x-2 ml-4">
                  <button
                    @click="toggleTodo(todo.id)"
                    class="bg-green-600 hover:bg-green-700 text-white p-2 rounded-lg transition-colors duration-200"
                    title="Mark as complete"
                  >
                    ✓
                  </button>
                  <button
                    @click="deleteTodo(todo.id)"
                    class="bg-red-600 hover:bg-red-700 text-white p-2 rounded-lg transition-colors duration-200"
                    title="Delete task"
                  >
                    ✕
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Completed Todos -->
        <div class="bg-gray-800 rounded-lg p-6 shadow-lg">
          <h2 class="text-2xl font-semibold mb-4 text-green-400">
            Completed ({{ completedTodos.length }})
          </h2>
          <div v-if="completedTodos.length === 0" class="text-gray-400 text-center py-8">
            No completed tasks yet.
          </div>
          <div v-else class="space-y-3">
            <div
              v-for="todo in completedTodos"
              :key="todo.id"
              class="bg-gray-700 rounded-lg p-4 border-l-4 border-green-400 opacity-75"
            >
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <h3 class="font-medium text-white line-through">{{ todo.title }}</h3>
                  <p v-if="todo.description" class="text-gray-300 text-sm mt-1 line-through">
                    {{ todo.description }}
                  </p>
                </div>
                <div class="flex space-x-2 ml-4">
                  <button
                    @click="toggleTodo(todo.id)"
                    class="bg-yellow-600 hover:bg-yellow-700 text-white p-2 rounded-lg transition-colors duration-200"
                    title="Mark as incomplete"
                  >
                    ↺
                  </button>
                  <button
                    @click="deleteTodo(todo.id)"
                    class="bg-red-600 hover:bg-red-700 text-white p-2 rounded-lg transition-colors duration-200"
                    title="Delete task"
                  >
                    ✕
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Summary -->
      <div class="mt-8 text-center text-gray-400">
        <p>
          Total: {{ todos.length }} tasks | 
          Active: {{ activeTodos.length }} | 
          Completed: {{ completedTodos.length }}
        </p>
      </div>
    </div>
  </div>
</template>