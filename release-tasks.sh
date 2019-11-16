#!/bin/bash

echo "Running Release Tasks"

echo "Running Make Migrations"
python3 manage.py makemigrations

echo "Running seed"
python3 seed.py

echo "Running Migrations"
python3 manage.py migrate



echo "Done"