#!/bin/bash

set -e

echo "${0}: running migrations."

python manage.py makemigrations
python manage.py migrate

echo "${0}: running Server"
python manage.py runserver 0.0.0.0:8000