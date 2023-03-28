import {createRouter, createWebHistory} from 'vue-router'
import HomeApp from './components/HomeApp.vue'
import CreateApp from './components/CreateApp.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeApp
  },
  {
    path: '/',
    name: 'create',
    component: CreateApp
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes
}) 


export default router