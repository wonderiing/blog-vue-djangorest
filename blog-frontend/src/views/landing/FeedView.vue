<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4 mb-4" v-for="post in postArray" :key="post.id">
        <div class="card shadow-sm">
          <img src="#" class="card-img-top" alt="Card Image 1" />
          <div class="card-body">
            <h5 class="card-title">{{ post.user }}</h5>
            <p class="card-text">{{ post.content }}</p>
            <a href="#" class="btn btn-primary">{{ post.user }}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { generalGet } from '@/composables/generalGet'
import type { Note } from '@/interfaces/note.interface'
import { onMounted, ref } from 'vue'

const postArray = ref<Note[]>([])
const sumbitData = async () => {
  postArray.value = await generalGet('http://127.0.0.1:8000/api/note/')
  console.log(postArray.value)
}

//Cada que se monte el componente hara esto:
onMounted(() => {
  sumbitData()
})
</script>
