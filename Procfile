release: python manage.py migrate && django python3 seed.py 
web: gunicorn api.wsgi