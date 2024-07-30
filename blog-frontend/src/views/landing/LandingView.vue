<template>
  <div id="app" class="landing-page d-flex flex-column">
    <header class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">DevPost</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#">Platform</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Solutions</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Customer Stories</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Resources</a>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'login' }">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="btn btn-outline-light ml-2" :to="{ name: 'feed' }">Feed</RouterLink>
          </li>
        </ul>
      </div>
    </header>

    <div
      class="container-fluid main-content d-flex flex-column justify-content-center align-items-center text-center text-white"
    >
      <h1 class="display-4">Bienvenido a DevPost!</h1>
      <p class="lead">
        Un lugar dondre podras postear tus avances como desarrollador Front-End y Back-End
      </p>
      <RouterLink class="btn btn-outline-light btn-lg" :to="{ name: 'auth' }"
        >Get Started</RouterLink
      >
      <div class="mt-4"></div>
    </div>
  </div>
</template>

<script>
import '@/assets/landingview.css'
</script>
