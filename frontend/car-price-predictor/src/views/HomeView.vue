<script setup lang="ts">
import { useRouter } from 'vue-router'
import CarPriceForm from '@/components/CarPriceForm.vue'
import { usePredictionStore } from '@/stores/prediction'

const router = useRouter()
const predictionStore = usePredictionStore()

function handlePrediction(data: { make: string; model: string; year: number; mileage: number; fuelType: string; transmission: string; engineSize: number; doors: number }) {
  // TODO: Send to ML backend and get actual prediction
  // For now, generate a mock price based on car data
  const basePrice = 25000
  const yearFactor = (data.year - 2000) * 500
  const mileageFactor = -data.mileage * 0.05
  const mockPrice = Math.max(5000, basePrice + yearFactor + mileageFactor)
  
  predictionStore.setPrediction(data, mockPrice)
  router.push('/results')
}
</script>

<template>
  <CarPriceForm @submit="handlePrediction" />
</template>

