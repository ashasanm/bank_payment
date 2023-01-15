#!/bin/bash

set -e

echo "${0}: running migrations."

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8001