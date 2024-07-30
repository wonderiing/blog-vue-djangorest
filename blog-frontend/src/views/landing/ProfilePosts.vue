<template>
  <div class="card" style="width: 18rem" v-for="post in user_post" :key="post.id">
    <div class="card-body">
      <h5 class="card-title"></h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ post.title }}</h6>
      <p class="card-text">
        {{ post.short_desc }}
      </p>
      <RouterLink :to="{ name: 'post-info', params: { id: post.id } }" class="card-link"
        >Mas Informacion</RouterLink
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import type { MyPosts } from '@/interfaces/post.interface'
import { RouterLink } from 'vue-router'

defineProps<MyPosts>()
</script>
