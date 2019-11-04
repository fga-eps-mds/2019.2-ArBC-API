release: python manage.py migrate
web: gunicorn api.wsgi --preload --workers --log-file
