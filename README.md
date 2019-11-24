[![pipeline status](https://gitlab.com/lucianosz7/2019-2-ArBC-API/badges/develop/pipeline.svg)](https://gitlab.com/lucianosz7/2019-2-ArBC-API/commits/develop) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9d9050f6e7a8428190c5cc25e3b815ae)](https://www.codacy.com/manual/ArBC/2019.2-ArBC-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fga-eps-mds/2019.2-ArBC-API&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/9d9050f6e7a8428190c5cc25e3b815ae)](https://www.codacy.com/manual/ArBC/2019.2-ArBC-API?utm_source=github.com&utm_medium=referral&utm_content=fga-eps-mds/2019.2-ArBC-API&utm_campaign=Badge_Coverage)

# ArBC-API

## Construir o projeto

sudo docker-compose -f local.yml build

## Criar as migrações

sudo docker-compose -f local.yml run --rm django python3 manage.py makemigrations

## Rodar as migrações

sudo docker-compose -f local.yml run --rm django python3 manage.py migrate

## Criar um super usuário

sudo docker-compose -f local.yml run --rm django python3 manage.py createsuperuser

## Gerar seedings

sudo docker-compose -f local.yml run --rm django python3 seeds.py

## Testar o linting

sudo docker-compose -f local.yml run --rm django flake8 --exclude=__init__.py

## Verificar os testes unitários

sudo docker-compose -f local.yml run --rm django python3 ./manage.py test

## Rodar cobertura de código

sudo docker-compose -f local.yml run --rm django python3 ./manage.py test && python-codacy-coverage -r coverage.xml

## Rodar o servidor

sudo docker-compose -f local.yml up

## Para acessar, abra no navegador em

localhost:8000/api
