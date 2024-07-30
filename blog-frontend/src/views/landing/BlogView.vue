<template>
  <div>
    <div class="container mt-5 pt-5">
      <h1 class="mb-4">Agrega un Nuevo Post</h1>
      <form @submit.prevent="sendPost">
        <div class="form-group">
          <label for="title">Titulo</label>
          <input type="text" class="form-control" id="title" required v-model="title" />
        </div>
        <div class="form-group">
          <label for="title">Añade una Descripcion</label>
          <input type="text" class="form-control" id="title" required v-model="shortDesc" />
        </div>
        <div class="form-group">
          <label for="content">Contenido</label>
          <textarea
            class="form-control"
            id="content"
            rows="10"
            cols="50"
            required
            v-model="content"
          >
          </textarea>
        </div>

        <div class="form-group">
          <label for="image">Image</label>
          <br />
          <input type="file" class="form-control-file" id="image" />
        </div>
        <br />
        <button type="submit" class="btn btn-primary">Add Post</button>
      </form>
      <hr />
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'

const title = ref('')
const shortDesc = ref('')
const content = ref('')
const user = ref(localStorage.getItem('id'))

const sendPost = async () => {
  const endpoint = 'http://127.0.0.1:8000/api/post/'
  const data = {
    title: title.value,
    short_desc: shortDesc.value,
    content: content.value,
    user: user.value
  }

  try {
    const response = await axios.post(endpoint, data)
    return response.data
  } catch (err) {
    console.error(err)
  }
}
</script>
