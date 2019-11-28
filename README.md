[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/fga-eps-mds/2019.2-ArBC-API.svg)](http://isitmaintained.com/project/fga-eps-mds/2019.2-ArBC-API "Average time to resolve an issue")[![Percentage of issues still open](http://isitmaintained.com/badge/open/fga-eps-mds/2019.2-ArBC-API.svg)](http://isitmaintained.com/project/fga-eps-mds/2019.2-ArBC-API "Percentage of issues still open")[![pipeline status](https://gitlab.com/lucianosz7/2019-2-ArBC-API/badges/master/pipeline.svg)](https://gitlab.com/lucianosz7/2019-2-ArBC-API/commits/master)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9d9050f6e7a8428190c5cc25e3b815ae)](https://www.codacy.com/manual/ArBC/2019.2-ArBC-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fga-eps-mds/2019.2-ArBC-API&amp;utm_campaign=Badge_Grade)[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/9d9050f6e7a8428190c5cc25e3b815ae)](https://www.codacy.com/manual/ArBC/2019.2-ArBC-API?utm_source=github.com&utm_medium=referral&utm_content=fga-eps-mds/2019.2-ArBC-API&utm_campaign=Badge_Coverage)


![](https://jlucassr.github.io/ArBC-Pages/imagens/logo.jpg)

## Porquê do Nome?
- “Ar” vem de um acrônimo para Augmented Reality (AR), realidade aumentada em inglês.
- “ABC” vem como um símbolo para alfabetização.

## O Mascote
   A Arara, por suas belas cores traz um visual lúdico e calmo que agrada pessoas, principalmente crianças. Logo a arara se torna um mascote excelente de um projeto com o objetivo de alfabetização. Também faz a referência do acrônimo AR como o nome da ave.
   
## Sobre
 O ArBC é uma aplicação web baseada nas APIs de RA (Realidade Aumentada) [AR.js](https://github.com/jeromeetienne/AR.js/) e [A-Frame](https://aframe.io/), que tem como objetivo tornar o processo de alfabetização mais interativo e engajante por meio desta tecnologia.
 A aplicação possui um front-end baseado no Vue.js (com a biblioteca [Vuex](https://vuex.vuejs.org/)) e [back-end](https://github.com/fga-eps-mds/2019.2-ArBC-API/) baseado em Django.

## Principais funcionalidades

-  Reconhecimento de letras através de patterns de RA.
-  Reconhecimento de palavras utilizando estas mesmas letras.
-  Visualização de imagens em cima da pattern ou palavra       reconhecida em tempo real.


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

sudo docker-compose -f local.yml run --rm django python3 manage.py test

## Rodar cobertura de código

sudo docker-compose -f local.yml run --rm django coverage run --source=app manage.py test

## Rodar o servidor

sudo docker-compose -f local.yml up

## Para acessar, abra no navegador em

localhost:8000/api
# Membros

## Equipe de EPS
||**Membros**|**E-mail**|**GitHub**|
|:-:|:-:|:-:|:-:|
|<img src="https://i.ibb.co/4gqXmYg/eduardolima.png" width="100" height="100"/>|Eduardo Lima|eduardolimrib@gmail.com|[@Eduardolimr](https://github.com/Eduardolimr)|
|<img src="https://i.ibb.co/xGd3zdH/joaolucas.png" width="100" height="100"/>|João Lucas|joao.lucas.ssr@gmail.com|[@jlucassr](https://github.com/jlucassr)|
|<img src="https://i.ibb.co/NxTMn7m/lucianosantos.png" width="100" height="100"/>|Luciano Santos|Luciano_z7@hotmail.com|[@lucianosz7](https://github.com/lucianosz7)|


## Equipe de MDS

||**Membros**|**E-mail**|**GitHub**|
|:-:|:-:|:-:|:-:|
|<img src="https://i.ibb.co/s9Vr8qc/igor.png" width="100" height="100"/>|Igor Batista|igorbatistapaiva@outlook.com|[@igor-paiva](https://github.com/igor-paiva)|
|<img src="https://i.ibb.co/Wft4bC6/joaohenrique.png" width="100" height="100"/>|João Henrique|joao.henrique1299@gmail.com|[@JoaoHenrique12](https://github.com/JoaoHenrique12)|
|<img src="https://i.ibb.co/0X55hLW/marcelo.png" width="100" height="100"/>|Marcelo Victor|marcelovictorg2@gmail.com|[@marcelog5](https://github.com/marcelog5)|
|<img src="https://i.ibb.co/mhCz5gb/rhuan.png" width="100" height="100"/>|Rhuan Carlos|rhuancarlos.queiroz@gmail.com|[@Rhuancpq](https://github.com/Rhuancpq)|
|<img src="https://i.ibb.co/2P6p1Vx/sergio.png" width="100" height="100"/>|Sérgio Almeida|sergiosacj@hotmail.com.br|[@SergioAlmeidaCiprianoJr](https://github.com/SergioAlmeidaCiprianoJr)|
|<img src="https://i.ibb.co/741s3JW/thiago.png" width="100" height="100"/>|Thiago Santos|thiago.lopes.santos.tls@gmail.com|[@thiagolopess](https://github.com/thiagolopess)|

## Licença
ArBC é distribuído sob a licença GPL v3.0. Consulte nosso arquivo [LICENSE](https://github.com/fga-eps-mds/2019.2-ArBC/blob/da5b0706c50af1bbc65694b5e0bf8d5d97d0e03b/LICENSE) para saber mais.
