# Tropical Cyclone Prediction System

A Django-powered web application that uses Machine Learning (Random Forest) to predict cyclone wind speeds and forecast potential cyclone tracks based on input features like central pressure, latitude, and longitude.

## 🚀 Features
- **Wind Speed Prediction**: Accurate estimation using a pre-trained Random Forest model.
- **Trend-based Forecasting**: Predicts future cyclone paths based on current movement trends.
- **Interactive Visualization**: Real-time map visualization using Leaflet.js.
- **Dynamic UI**: Responsive dashboard built with Tailwind CSS and React.
- **PDF Reports**: Generate downloadable reports for cyclone predictions.

## 🛠️ Tech Stack
- **Backend**: Python (Django), Gunicorn
- **Machine Learning**: Scikit-learn, NumPy, Joblib
- **Frontend**: React (via CDN), Tailwind CSS, Leaflet.js, Chart.js
- **Static Assets**: Whitenoise for efficient production serving

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd cyclone_prediction
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
   *Edit the `.env` file to include your unique `SECRET_KEY` and other settings.*

5. **Initialize the Database**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## 🚢 Deployment Guide

The project is pre-configured for platforms like Heroku, Render, or Railway.

1. **Static Files**: Run `python manage.py collectstatic` to prepare assets.
2. **Server**: The `Procfile` uses `gunicorn` to serve the WSGI application.
3. **Database**: `dj-database-url` automatically configures the database based on your environment's `DATABASE_URL`.
4. **Environment Variables**: Ensure you set `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` on your hosting provider's dashboard.

## 🧪 Testing
Run the test suite to verify the application:
```bash
python manage.py test predictor


⚠️ Model file not included due to GitHub size limits.
It is automatically downloaded when the app runs.
```
