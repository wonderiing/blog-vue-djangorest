<template>
  <!-- Section: Design Block -->
  <h2 class="fw-bold mb-5">Sign up now</h2>

  <section class="text-center">
    <form @submit.prevent="submitRegiser">
      <!-- 2 column grid layout with text inputs for the first and last names -->
      <div class="row">
        <div class="col-md-6 mb-4">
          <div data-mdb-input-init class="form-outline">
            <input type="text" id="form3Example1" class="form-control" v-model="first_name" />
            <label class="form-label" for="form3Example1">First name</label>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div data-mdb-input-init class="form-outline">
            <input type="text" id="form3Example2" class="form-control" v-model="last_name" />
            <label class="form-label" for="form3Example2">Last name</label>
          </div>
        </div>
      </div>

      <!-- Email input -->
      <div data-mdb-input-init class="form-outline mb-4">
        <input type="email" id="form3Example3" class="form-control" v-model="email" />
        <label class="form-label" for="form3Example3">Email address</label>
      </div>

      <!-- Email input -->
      <div data-mdb-input-init class="form-outline mb-4">
        <input type="text" id="form3Example3" class="form-control" v-model="nickname" />
        <label class="form-label" for="form3Example3">Nickname</label>
      </div>

      <!-- Password input -->
      <div data-mdb-input-init class="form-outline mb-4">
        <input type="password" id="form3Example4" class="form-control" v-model="password" />
        <label class="form-label" for="form3Example4">Password</label>
      </div>

      <!-- Submit button -->
      <button
        type="submit"
        data-mdb-button-init
        data-mdb-ripple-init
        class="btn btn-primary btn-block mb-4"
      >
        Sign up
      </button>
      <br />
      <RouterLink class="btn btn-success" :to="{ name: 'login' }">Or Login Here</RouterLink>
    </form>
  </section>
  <!-- Section: Design Block -->
</template>

<script setup lang="ts">
import { useRegister } from '@/composables/useRegister'

const { email, last_name, first_name, password, nickname, submitRegiser } = useRegister()
</script>
