#!/bin/bash

# scripts/start_server.sh

# Activate the Python virtual environment
source venv/bin/activate

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver 0.0.0.0:8000
