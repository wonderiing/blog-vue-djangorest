<!-- src/components/Sidebar.vue -->
<template>
  <div class="app-container">
    <div class="sidebar">
      <nav class="nav flex-column">
        <RouterLink class="nav-link" :to="{ name: 'home' }">Home</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'post' }">Postea</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'feed' }">Feed</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'posts' }">Posts</RouterLink>
      </nav>
      <div class="sidebar-footer">
        <img
          :src="'http://127.0.0.1:8000/' + userData?.profile_picture"
          alt="Profile Image"
          class="profile-image"
        />
        <br />
        <RouterLink class="nickname" :to="{ name: 'profile' }">{{ userData?.nickname }}</RouterLink>
        <p v-if="token"></p>
        <RouterLink v-else :to="{ name: 'login' }" class="btn btn-primary btn-block"
          >Login</RouterLink
        >
        <RouterLink @click="logout" :to="{ name: 'home' }" class="btn btn-secondary btn-block"
          >Logout</RouterLink
        >
      </div>
    </div>
    <div class="main-content">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script setup lang="ts">
import { getUserInfo } from '@/composables/getUserInfo'
import { onMounted, ref } from 'vue'
import type { UserInformation } from '@/interfaces/users.interface'
import '@/assets/sidebar.css'
const token = localStorage.getItem('accessToken')

const logout = () => {
  localStorage.clear()
}

const userData = ref<UserInformation>()
const getData = async () => {
  userData.value = await getUserInfo('http://127.0.0.1:8000/users/usersinfo/')
}

onMounted(async () => {
  await getData()
})
</script>
