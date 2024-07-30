<template>
  <h2 class="fw-bold mb-5">Login</h2>
  <form @submit.prevent="sumbitData">
    <!-- 2 column grid layout with text inputs for the first and last names -->

    <!-- Email input -->
    <div data-mdb-input-init class="form-outline mb-4">
      <input type="email" id="form3Example3" class="form-control" v-model="email" />
      <label class="form-label" for="form3Example3">Email address</label>
    </div>

    <!-- Password input -->
    <div data-mdb-input-init class="form-outline mb-4">
      <input type="password" id="form3Example4" class="form-control" v-model="password" />
      <label class="form-label" for="form3Example4">Password</label>
    </div>

    <!-- Checkbox -->
    <div class="form-check d-flex justify-content-center mb-4">
      <input class="form-check-input me-2" type="checkbox" value="" id="form2Example33" checked />
      <label class="form-check-label" for="form2Example33"> Remember Me </label>
    </div>

    <!-- Submit button -->
    <button
      data-mdb-button-init
      data-mdb-ripple-init
      class="btn btn-primary btn-block mb-4"
      @click="sumbitData"
    >
      Login
    </button>
    <br />
    <RouterLink class="btn btn-success" :to="{ name: 'register' }">Or Register Here</RouterLink>
  </form>
</template>

<script setup lang="ts">
import { useLogin } from '@/composables/useLogin'

const { email, password, sumbitData } = useLogin()
</script>
