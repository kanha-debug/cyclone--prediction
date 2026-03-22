#!/bin/bash
set -e

cd cyclone_prediction

python manage.py migrate --noinput

exec gunicorn cyclone_prediction.wsgi --bind 0.0.0.0:8000 --log-file -
