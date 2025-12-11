<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import PredictionResult from '@/components/PredictionResult.vue'
import { usePredictionStore } from '@/stores/prediction'

const router = useRouter()
const predictionStore = usePredictionStore()

onMounted(() => {
  // Redirect to home if no prediction data
  if (!predictionStore.carData || !predictionStore.predictedPrice) {
    router.replace('/')
  }
})

function handleNewPrediction() {
  predictionStore.clearPrediction()
  router.push('/')
}
</script>

<template>
  <PredictionResult
    v-if="predictionStore.carData && predictionStore.predictedPrice"
    :price="predictionStore.predictedPrice"
    :car-data="predictionStore.carData"
    @new-prediction="handleNewPrediction"
  />
</template>

