import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/landing/LandingView.vue'
import isAuthenticated from '@/guards/jwt.guard'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingView
    },
    {
      path: '/auth',
      name: 'auth',
      redirect: { name: 'login' },
      component: () => import('@/views/auth/LayoutAuth.vue'),
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('@/views/auth/LoginView.vue')
        },
        {
          path: 'register',
          name: 'register',
          component: () => import('@/views/auth/RegisterView.vue')
        }
      ]
    },
    {
      path: '/blog',
      name: 'blog',
      redirect: { name: 'feed' },
      beforeEnter: [isAuthenticated],
      component: () => import('@/views/landing/SideBar.vue'),
      children: [
        {
          path: 'add-post',
          name: 'post',
          beforeEnter: [isAuthenticated],
          component: () => import('@/views/landing/BlogView.vue')
        },
        {
          path: 'feed',
          name: 'feed',
          component: () => import('@/views/landing/FeedView.vue')
        },
        {
          path: 'posts',
          name: 'posts',
          component: () => import('@/views/landing/PostView.vue')
        },
        {
          path: 'posts/:id',
          name: 'post-info',
          component: () => import('@/views/landing/PostComplete.vue')
        },
        {
          path: 'profile',
          name: 'profile',
          component: () => import('@/views/landing/MyProfile.vue')
        }
      ]
    }
  ]
})

export default router
