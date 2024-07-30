<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-header">
        <h3>Perfil de Usuario</h3>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-md-4">
            <img
              :src="'http://127.0.0.1:8000/' + userData?.profile_picture"
              alt="Profile Image"
              class="img-fluid rounded-circle mb-3"
            />
          </div>
          <div class="col-md-8">
            <h4>Name</h4>
            <p><strong>Email:</strong> {{ userData?.email }}</p>
            <p><strong>Username:</strong> {{ userData?.nickname }}</p>
            <p><strong>Posts:</strong><ProfilePosts :user_post="userData?.user_post ?? []" /></p>
            <!-- Agrega más campos según tus necesidades -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { getUserInfo } from '@/composables/getUserInfo'
import { onMounted, ref } from 'vue'
import type { UserInformation } from '@/interfaces/users.interface'
import ProfilePosts from './ProfilePosts.vue'
import '@/assets/myprofile.css'

const userData = ref<UserInformation>()

const getData = async () => {
  userData.value = await getUserInfo('http://127.0.0.1:8000/users/usersinfo/')
}

onMounted(async () => {
  await getData()
})
</script>
