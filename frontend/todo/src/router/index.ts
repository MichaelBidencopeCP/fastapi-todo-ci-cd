import { createRouter, createWebHistory } from 'vue-router'
import todo from '@/views/todo.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'todo',
      component: todo
    }
  ],
})

export default router
