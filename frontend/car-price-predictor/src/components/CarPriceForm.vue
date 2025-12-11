<script setup lang="ts">
import { ref, computed } from 'vue'

interface CarFormData {
  make: string
  model: string
  year: number
  mileage: number
  fuelType: string
  transmission: string
  engineSize: number
  doors: number
}

const emit = defineEmits<{
  submit: [data: CarFormData]
}>()

const currentYear = new Date().getFullYear()

const form = ref<CarFormData>({
  make: '',
  model: '',
  year: currentYear,
  mileage: 0,
  fuelType: 'petrol',
  transmission: 'automatic',
  engineSize: 2.0,
  doors: 4
})

const carMakes = [
  'Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 
  'Kia', 'Lexus', 'Mazda', 'Mercedes-Benz', 'Nissan', 
  'Subaru', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo'
]

const fuelTypes = ['petrol', 'diesel', 'electric', 'hybrid']
const transmissions = ['automatic', 'manual']
const doorOptions = [2, 3, 4, 5]

const years = computed(() => {
  const yearsArray = []
  for (let y = currentYear + 1; y >= 1990; y--) {
    yearsArray.push(y)
  }
  return yearsArray
})

const isValid = computed(() => {
  return form.value.make && 
         form.value.model && 
         form.value.year && 
         form.value.mileage >= 0 &&
         form.value.engineSize > 0
})

const formattedMileage = computed(() => {
  return new Intl.NumberFormat().format(form.value.mileage)
})

function handleSubmit() {
  if (isValid.value) {
    emit('submit', { ...form.value })
  }
}

function resetForm() {
  form.value = {
    make: '',
    model: '',
    year: currentYear,
    mileage: 0,
    fuelType: 'petrol',
    transmission: 'automatic',
    engineSize: 2.0,
    doors: 4
  }
}
</script>

<template>
  <div class="form-container">
    <div class="form-header">
      <div class="icon-wrapper">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="car-icon">
          <path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/>
        </svg>
      </div>
      <h2>Car Details</h2>
      <p class="subtitle">Enter your vehicle information to get an estimated price</p>
    </div>

    <form @submit.prevent="handleSubmit" class="car-form">
      <div class="form-grid">
        <!-- Make -->
        <div class="form-group">
          <label for="make">Make</label>
          <select id="make" v-model="form.make" required>
            <option value="" disabled>Select make</option>
            <option v-for="make in carMakes" :key="make" :value="make">
              {{ make }}
            </option>
          </select>
        </div>

        <!-- Model -->
        <div class="form-group">
          <label for="model">Model</label>
          <input 
            id="model" 
            v-model="form.model" 
            type="text" 
            placeholder="e.g. Camry, Civic, Model 3"
            required
          />
        </div>

        <!-- Year -->
        <div class="form-group">
          <label for="year">Year</label>
          <select id="year" v-model="form.year" required>
            <option v-for="year in years" :key="year" :value="year">
              {{ year }}
            </option>
          </select>
        </div>

        <!-- Mileage -->
        <div class="form-group">
          <label for="mileage">
            Mileage
            <span class="mileage-display">{{ formattedMileage }} mi</span>
          </label>
          <input 
            id="mileage" 
            v-model.number="form.mileage" 
            type="range" 
            min="0" 
            max="300000" 
            step="1000"
          />
          <div class="range-labels">
            <span>0</span>
            <span>300k</span>
          </div>
        </div>

        <!-- Fuel Type -->
        <div class="form-group">
          <label>Fuel Type</label>
          <div class="button-group">
            <button 
              v-for="fuel in fuelTypes" 
              :key="fuel"
              type="button"
              :class="['option-btn', { active: form.fuelType === fuel }]"
              @click="form.fuelType = fuel"
            >
              {{ fuel }}
            </button>
          </div>
        </div>

        <!-- Transmission -->
        <div class="form-group">
          <label>Transmission</label>
          <div class="button-group">
            <button 
              v-for="trans in transmissions" 
              :key="trans"
              type="button"
              :class="['option-btn', { active: form.transmission === trans }]"
              @click="form.transmission = trans"
            >
              {{ trans }}
            </button>
          </div>
        </div>

        <!-- Engine Size -->
        <div class="form-group">
          <label for="engineSize">Engine Size (L)</label>
          <input 
            id="engineSize" 
            v-model.number="form.engineSize" 
            type="number" 
            min="0.5" 
            max="8.0" 
            step="0.1"
            placeholder="2.0"
          />
        </div>

        <!-- Doors -->
        <div class="form-group">
          <label>Doors</label>
          <div class="button-group compact">
            <button 
              v-for="door in doorOptions" 
              :key="door"
              type="button"
              :class="['option-btn', { active: form.doors === door }]"
              @click="form.doors = door"
            >
              {{ door }}
            </button>
          </div>
        </div>
      </div>

      <div class="form-actions">
        <button type="button" class="btn-secondary" @click="resetForm">
          Reset
        </button>
        <button type="submit" class="btn-primary" :disabled="!isValid">
          <span>Get Price Estimate</span>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="arrow-icon">
            <path fill-rule="evenodd" d="M3 10a.75.75 0 01.75-.75h10.638L10.23 5.29a.75.75 0 111.04-1.08l5.5 5.25a.75.75 0 010 1.08l-5.5 5.25a.75.75 0 11-1.04-1.08l4.158-3.96H3.75A.75.75 0 013 10z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.form-container {
  background: linear-gradient(135deg, var(--color-background-soft) 0%, var(--color-background-mute) 100%);
  border-radius: 24px;
  padding: 2.5rem;
  max-width: 680px;
  margin: 0 auto;
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -2px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  border: 1px solid var(--color-border);
}

.form-header {
  text-align: center;
  margin-bottom: 2rem;
}

.icon-wrapper {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  box-shadow: 0 8px 16px -4px rgba(16, 185, 129, 0.4);
}

.car-icon {
  width: 32px;
  height: 32px;
  color: white;
}

.form-header h2 {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.subtitle {
  color: var(--color-text);
  opacity: 0.7;
  font-size: 0.95rem;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-text);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.mileage-display {
  font-weight: 700;
  color: #10b981;
  font-size: 0.9rem;
}

input[type="text"],
input[type="number"],
select {
  padding: 0.875rem 1rem;
  border-radius: 12px;
  border: 2px solid var(--color-border);
  background: var(--color-background);
  color: var(--color-text);
  font-size: 1rem;
  transition: all 0.2s ease;
  outline: none;
}

input[type="text"]:focus,
input[type="number"]:focus,
select:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);
}

input[type="text"]::placeholder {
  color: var(--color-text);
  opacity: 0.4;
}

select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%236b7280'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 1.25rem;
  padding-right: 2.5rem;
}

input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 8px;
  border-radius: 4px;
  background: var(--color-border);
  outline: none;
  cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4);
  transition: transform 0.2s ease;
}

input[type="range"]::-webkit-slider-thumb:hover {
  transform: scale(1.1);
}

input[type="range"]::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  cursor: pointer;
  border: none;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4);
}

.range-labels {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--color-text);
  opacity: 0.5;
  margin-top: -0.25rem;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.button-group.compact {
  gap: 0.375rem;
}

.option-btn {
  flex: 1;
  min-width: fit-content;
  padding: 0.75rem 1rem;
  border-radius: 10px;
  border: 2px solid var(--color-border);
  background: var(--color-background);
  color: var(--color-text);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: capitalize;
}

.button-group.compact .option-btn {
  padding: 0.625rem 0.875rem;
  min-width: 48px;
}

.option-btn:hover {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.05);
}

.option-btn.active {
  border-color: #10b981;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.15) 100%);
  color: #10b981;
  font-weight: 600;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--color-border);
}

.btn-primary,
.btn-secondary {
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
}

.btn-primary {
  flex: 1;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  box-shadow: 0 4px 14px -3px rgba(16, 185, 129, 0.5);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px -4px rgba(16, 185, 129, 0.6);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.arrow-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.2s ease;
}

.btn-primary:hover:not(:disabled) .arrow-icon {
  transform: translateX(4px);
}

.btn-secondary {
  background: transparent;
  color: var(--color-text);
  border: 2px solid var(--color-border);
}

.btn-secondary:hover {
  border-color: var(--color-border-hover);
  background: var(--color-background-mute);
}

@media (max-width: 640px) {
  .form-container {
    padding: 1.5rem;
    border-radius: 16px;
  }

  .form-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .form-header h2 {
    font-size: 1.5rem;
  }

  .form-actions {
    flex-direction: column-reverse;
  }

  .btn-secondary {
    width: 100%;
  }
}
</style>

