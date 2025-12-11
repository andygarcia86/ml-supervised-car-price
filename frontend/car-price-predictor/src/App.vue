<script setup lang="ts">
import CarPriceForm from './components/CarPriceForm.vue'

function handlePrediction(data: { make: string; model: string; year: number; mileage: number; fuelType: string; transmission: string; engineSize: number; doors: number }) {
  console.log('Predicting price for:', data)
  // TODO: Send to ML backend
}
</script>

<template>
  <main class="app-container">
    <CarPriceForm @submit="handlePrediction" />
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
