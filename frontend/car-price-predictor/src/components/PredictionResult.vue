<script setup lang="ts">
import { computed } from 'vue'

interface CarData {
  make: string
  model: string
  year: number
  mileage: number
  fuelType: string
  transmission: string
  engineSize: number
  doors: number
}

const props = defineProps<{
  price: number
  carData: CarData
}>()

const emit = defineEmits<{
  newPrediction: []
}>()

const formattedPrice = computed(() => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(props.price)
})

const formattedMileage = computed(() => {
  return new Intl.NumberFormat().format(props.carData.mileage)
})

const priceRange = computed(() => {
  const low = props.price * 0.9
  const high = props.price * 1.1
  const format = (n: number) => new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(n)
  return { low: format(low), high: format(high) }
})
</script>

<template>
  <div class="result-container">
    <div class="result-header">
      <div class="success-icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm13.36-1.814a.75.75 0 10-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.14-.094l3.75-5.25z" clip-rule="evenodd" />
        </svg>
      </div>
      <h2>Estimated Value</h2>
      <p class="subtitle">Based on current market data</p>
    </div>

    <div class="price-display">
      <span class="price">{{ formattedPrice }}</span>
      <div class="price-range">
        <span>Typical range: {{ priceRange.low }} – {{ priceRange.high }}</span>
      </div>
    </div>

    <div class="car-summary">
      <h3>Vehicle Details</h3>
      <div class="details-grid">
        <div class="detail-item">
          <span class="label">Make & Model</span>
          <span class="value">{{ carData.make }} {{ carData.model }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Year</span>
          <span class="value">{{ carData.year }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Mileage</span>
          <span class="value">{{ formattedMileage }} mi</span>
        </div>
        <div class="detail-item">
          <span class="label">Fuel Type</span>
          <span class="value capitalize">{{ carData.fuelType }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Transmission</span>
          <span class="value capitalize">{{ carData.transmission }}</span>
        </div>
        <div class="detail-item">
          <span class="label">Engine</span>
          <span class="value">{{ carData.engineSize }}L</span>
        </div>
      </div>
    </div>

    <div class="actions">
      <button class="btn-primary" @click="emit('newPrediction')">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="icon">
          <path fill-rule="evenodd" d="M15.312 11.424a5.5 5.5 0 01-9.201 2.466l-.312-.311h2.433a.75.75 0 000-1.5H3.989a.75.75 0 00-.75.75v4.242a.75.75 0 001.5 0v-2.43l.31.31a7 7 0 0011.712-3.138.75.75 0 00-1.449-.39zm1.23-3.723a.75.75 0 00.219-.53V2.929a.75.75 0 00-1.5 0v2.43l-.31-.31A7 7 0 003.239 8.188a.75.75 0 101.448.389A5.5 5.5 0 0113.89 6.11l.311.31h-2.432a.75.75 0 000 1.5h4.243a.75.75 0 00.53-.219z" clip-rule="evenodd" />
        </svg>
        New Prediction
      </button>
    </div>

    <div class="disclaimer">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="info-icon">
        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" />
      </svg>
      <p>This is an estimate based on machine learning predictions. Actual prices may vary based on condition, location, and market factors.</p>
    </div>
  </div>
</template>

<style scoped>
.result-container {
  background: linear-gradient(135deg, var(--color-background-soft) 0%, var(--color-background-mute) 100%);
  border-radius: 24px;
  padding: 2.5rem;
  max-width: 580px;
  margin: 0 auto;
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -2px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  border: 1px solid var(--color-border);
}

.result-header {
  text-align: center;
  margin-bottom: 1.5rem;
}

.success-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  box-shadow: 0 8px 16px -4px rgba(16, 185, 129, 0.4);
}

.success-icon svg {
  width: 36px;
  height: 36px;
  color: white;
}

.result-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 0.25rem;
  letter-spacing: -0.02em;
}

.subtitle {
  color: var(--color-text);
  opacity: 0.7;
  font-size: 0.9rem;
}

.price-display {
  text-align: center;
  padding: 2rem;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.1) 100%);
  border-radius: 16px;
  margin-bottom: 1.5rem;
  border: 2px solid rgba(16, 185, 129, 0.2);
}

.price {
  font-size: 3rem;
  font-weight: 800;
  color: #10b981;
  letter-spacing: -0.03em;
  line-height: 1;
  display: block;
  margin-bottom: 0.75rem;
}

.price-range {
  font-size: 0.875rem;
  color: var(--color-text);
  opacity: 0.7;
}

.car-summary {
  margin-bottom: 1.5rem;
}

.car-summary h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-heading);
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--color-border);
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.detail-item .label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text);
  opacity: 0.6;
}

.detail-item .value {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text);
}

.capitalize {
  text-transform: capitalize;
}

.actions {
  margin-bottom: 1.5rem;
}

.btn-primary {
  width: 100%;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  box-shadow: 0 4px 14px -3px rgba(16, 185, 129, 0.5);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px -4px rgba(16, 185, 129, 0.6);
}

.btn-primary .icon {
  width: 18px;
  height: 18px;
}

.disclaimer {
  display: flex;
  gap: 0.75rem;
  padding: 1rem;
  background: var(--color-background-mute);
  border-radius: 12px;
  border: 1px solid var(--color-border);
}

.info-icon {
  width: 20px;
  height: 20px;
  color: var(--color-text);
  opacity: 0.5;
  flex-shrink: 0;
  margin-top: 0.125rem;
}

.disclaimer p {
  font-size: 0.8rem;
  color: var(--color-text);
  opacity: 0.7;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 640px) {
  .result-container {
    padding: 1.5rem;
    border-radius: 16px;
  }

  .price {
    font-size: 2.5rem;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }
}
</style>

