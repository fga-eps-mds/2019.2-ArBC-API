# ArBC-API

## Construir o projeto

sudo docker-compose -f local.yml build

## Criar as migrações

sudo docker-compose -f local.yml run --rm 
django python3 manage.py makemigrations

## Rodar as migrações

sudo docker-compose -f local.yml run --rm django python3 manage.py migrate

## Criar um super usuário

sudo docker-compose -f local.yml run --rm django python3 manage.py createsuperuser

## Gerar seedings

sudo docker-compose -f local.yml run --rm django python3 seed.py

## Testar o linting

sudo docker-compose -f local.yml run --rm django flake8

## Verificar os testes unitários

sudo docker-compose -f local.yml run --rm django py.test

## Rodar o servidor

sudo docker-compose -f local.yml up

## Para acessar, abra no navegador em

localhost:8000/api
