#!/bin/bash

echo "Running Release Tasks"

#echo "Super User"
#python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('arbcAdmin', 'arbc.base@gmail.com', 'Arbc2019')"

echo "Running Make Migrations"
python3 manage.py makemigrations

#echo "Running seed"
#python3 seed.py

echo "Running Migrations"
python3 manage.py migrate

echo "Running Fake Migrations"
python3 manage.py migrate --fake


echo "Done"