<template>
  <div class="card" v-for="post in postsArray" :key="post.id">
    <h5 class="card-header">Por: {{ post.user }}</h5>
    <div class="card-body">
      <h5 class="card-title">{{ post.title }}</h5>
      <p class="card-text">
        {{ post.short_desc }}
      </p>
      <RouterLink :to="{ name: 'post-info', params: { id: post.id } }" class="btn btn-primary"
        >Leer Mas</RouterLink
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import { generalGet } from '@/composables/generalGet'
import type { UserPost } from '@/interfaces/users.interface'
import { onMounted, ref } from 'vue'

const postsArray = ref<UserPost[]>([])

const getPostData = async () => {
  try {
    const data = await generalGet('http://127.0.0.1:8000/api/post')
    postsArray.value = data
    console.log(postsArray.value)
  } catch (err) {
    console.error(err)
  }
}

onMounted(async () => {
  await getPostData()
})
</script>
