from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from .utils import load_files

# ✅ Load model once (important fix)
model, scaler = load_files()


def get_cyclone_category(wind_speed):
    if wind_speed < 34:
        return "Tropical Depression"
    elif wind_speed < 64:
        return "Tropical Storm"
    elif wind_speed < 83:
        return "Category 1 Hurricane"
    elif wind_speed < 96:
        return "Category 2 Hurricane"
    elif wind_speed < 113:
        return "Category 3 Hurricane"
    elif wind_speed < 137:
        return "Category 4 Hurricane"
    else:
        return "Category 5 Hurricane"


def predict_future_path(history):
    if len(history) < 2:
        return []

    p2 = history[-1]
    p1 = history[-2]

    lat_diff = p2['latitude'] - p1['latitude']
    lon_diff = p2['longitude'] - p1['longitude']

    forecasts = []
    intervals = [6, 12, 24, 48]
    base_hours = p2.get('number_of_hours', 6) or 6

    for hours in intervals:
        multiplier = hours / base_hours
        curve_lat = (multiplier ** 1.1) * lat_diff
        curve_lon = (multiplier ** 1.1) * lon_diff

        forecasts.append({
            'hours': hours,
            'latitude': round(p2['latitude'] + curve_lat, 2),
            'longitude': round(p2['longitude'] + curve_lon, 2),
            'type': 'forecast'
        })

    return forecasts


def predict(request):
    if request.method == 'POST':
        try:
            import json

            # Handle JSON or form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            features = [
                float(data['international_number_id']),
                float(data['tropical_cyclone_number']),
                float(data['tropical_cyclone_end_record']),
                float(data['number_of_hours']),
                float(data['grade']),
                float(data['latitude']),
                float(data['longitude']),
                float(data['minimum_central_pressure'])
            ]

            # ✅ Use preloaded model
            features_scaled = scaler.transform([features])
            prediction = float(model.predict(features_scaled)[0])
            category = get_cyclone_category(prediction)

            # Forecast
            history_data = data.get('history', [])
            current_point = {
                'latitude': float(data['latitude']),
                'longitude': float(data['longitude']),
                'number_of_hours': float(data['number_of_hours'])
            }

            forecast_history = history_data + [current_point]
            forecasts = predict_future_path(forecast_history)

            # JSON response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', ''):
                return JsonResponse({
                    'prediction': round(prediction, 2),
                    'category': category,
                    'forecasts': forecasts
                })

            # HTML response
            return render(request, 'predictor/result.html', {
                'prediction': prediction,
                'category': category,
                'forecasts': forecasts,
                'latitude': data['latitude'],
                'longitude': data['longitude']
            })

        except Exception as e:
            return JsonResponse({'error': f'Prediction error: {str(e)}'}, status=400)

    return render(request, 'predictor/form.html')