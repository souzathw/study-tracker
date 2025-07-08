import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import Study from '../views/Study.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/Login', name: 'Login', component: Login },
  { path: '/Register', name: 'Register', component: Register },
  { path: '/Dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/Study', name: 'Study', component: Study },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/register']
  const authRequired = !publicPages.includes(to.path)
  const token = localStorage.getItem('token')

  if (authRequired && !token) {
    return next('/login')
  }

  next()
})

export default router
