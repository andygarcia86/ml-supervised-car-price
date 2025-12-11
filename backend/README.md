# Car Price Predictor - Backend API

Flask-based REST API for the Car Price Prediction machine learning model.

## Tech Stack

- **Python 3.x**
- **Flask** - Web framework
- **ML Libraries** - (to be added: scikit-learn, pandas, numpy)

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   └── main.py          # Flask application entry point
├── requirements.txt     # Python dependencies
└── README.md
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Server

### Development

```bash
python app/main.py
```

Or using Flask CLI:

```bash
flask --app app.main run --debug
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check

```
GET /
```

Returns a welcome message to verify the API is running.

**Response:**
```json
{
  "message": "Hello from your Flask API!"
}
```

### Predict Price (Coming Soon)

```
POST /predict
```

Predicts the price of a car based on its features.

**Request Body:**
```json
{
  "make": "Toyota",
  "model": "Camry",
  "year": 2020,
  "mileage": 35000,
  "fuelType": "petrol",
  "transmission": "automatic",
  "engineSize": 2.5,
  "doors": 4
}
```

**Response:**
```json
{
  "predictedPrice": 25000,
  "confidence": 0.85
}
```

## Development

### Adding ML Model

1. Train your model using the dataset in `/datasets`
2. Save the trained model (e.g., using `joblib` or `pickle`)
3. Load the model in the Flask app
4. Create prediction endpoint

## Environment Variables

Create a `.env` file for configuration:

```
FLASK_ENV=development
FLASK_DEBUG=1
MODEL_PATH=./models/car_price_model.pkl
```

