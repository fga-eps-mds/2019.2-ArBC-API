#!/bin/bash

echo "Running Release Tasks"

echo "Super User"
./manage.py createsuperuser2 --username arbcAdmin --password Arbc2019 --noinput --email 'arbc.base@gmail.com'

echo "Running Make Migrations"
python3 manage.py makemigrations

echo "Running seed"
python3 seed.py

echo "Running Migrations"
python3 manage.py migrate



echo "Done"