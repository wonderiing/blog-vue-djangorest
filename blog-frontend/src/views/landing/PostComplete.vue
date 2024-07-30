<template>
  <div class="card text-center">
    <div class="card-header">{{ postData?.user }}</div>
    <div class="card-body">
      <h5 class="card-title">{{ postData?.title }}</h5>
      <p class="card-text">
        {{ postData?.content }}
      </p>

      <img v-if="postData?.image !== null" :src="'http://127.0.0.1:8000' + postData?.image" />
      <br />

      <RouterLink :to="{ name: 'posts' }" class="btn btn-primary">Regresar</RouterLink>
    </div>
    <div class="card-footer text-muted">2 days ago</div>
  </div>
</template>

<script setup lang="ts">
import { generalGet } from '@/composables/generalGet'
import type { UserPost } from '@/interfaces/users.interface'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const postData = ref<UserPost>()
const route = useRoute()

const getData = async () => {
  try {
    const data = await generalGet(`http://127.0.0.1:8000/api/post/${route.params.id}`)
    postData.value = data
    console.log(postData.value)
  } catch (err) {
    console.error(err)
  }
}

onMounted(async () => {
  await getData()
})
</script>
