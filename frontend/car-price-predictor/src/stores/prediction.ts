import { ref } from 'vue'
import { defineStore } from 'pinia'

export interface CarData {
  make: string
  model: string
  year: number
  mileage: number
  fuelType: string
  transmission: string
  engineSize: number
  doors: number
}

export const usePredictionStore = defineStore('prediction', () => {
  const carData = ref<CarData | null>(null)
  const predictedPrice = ref<number | null>(null)

  function setPrediction(car: CarData, price: number) {
    carData.value = car
    predictedPrice.value = price
  }

  function clearPrediction() {
    carData.value = null
    predictedPrice.value = null
  }

  return { carData, predictedPrice, setPrediction, clearPrediction }
})

