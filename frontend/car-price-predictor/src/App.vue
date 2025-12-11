<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <main class="app-container">
    <RouterView />
  </main>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
</style>
