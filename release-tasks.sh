#!/bin/bash

echo "Running Release Tasks"

#echo "Removing migrations" 
#find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "*/migrations/*.pyc"  -delete

echo "Running Make Migrations"
python3 manage.py makemigrations

#Run only when you need to populate the database
#echo "Running seed"
#python3 seed.py

echo "Running Migrations"
python3 manage.py migrate

echo "Running Fake Migrations"
python3 manage.py migrate --fake


echo "Done"