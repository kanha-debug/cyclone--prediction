# Repository Guidelines

## Project Structure & Module Organization
This is a Django-based application for tropical cyclone prediction. It consists of a single app, `predictor`, and the main project configuration in `cyclone_prediction`.

- **predictor/**: Contains the core logic for cyclone prediction.
    - **models/**: Houses the pre-trained machine learning models (`random_forest_model.joblib` and `scaler.joblib`).
    - **templates/**: Contains the HTML templates for the web interface, utilizing Tailwind CSS, Leaflet.js, and React.
    - **views.py**: Implements prediction logic, including coordinate extrapolation and cyclone categorization.
- **cyclone_prediction/**: Project-level settings and URL routing.

The application uses a Random Forest model and a scaler to predict cyclone wind speeds based on input features like central pressure, latitude, and longitude. It also provides a trend-based forecasting mechanism for future cyclone paths.

## Build, Test, and Development Commands
The project follows standard Django command patterns. Ensure you have the necessary dependencies (`django`, `joblib`, `numpy`, `scikit-learn`) installed.

- **Run development server**: `python manage.py runserver`
- **Apply database migrations**: `python manage.py migrate`
- **Create new migrations**: `python manage.py makemigrations`
- **Run tests**: `python manage.py test`

## Coding Style & Naming Conventions
The project follows standard Python (PEP 8) and Django coding conventions. 
- Templates use a mix of Django template tags and client-side JavaScript (React, Tailwind CSS).
- Frontend libraries are loaded via CDN in `form.html`.

## Testing Guidelines
Tests are located in `predictor/tests.py`. Use the standard Django test runner: `python manage.py test predictor`.
