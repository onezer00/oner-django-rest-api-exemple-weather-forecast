# oner-django-rest-api-exemple-weather-forecast
## Exemplo simples de previsão do tempo com Django

Este é um simples exemplo de scrap para captura de dados de um site de previsão de tempo.

Esta mini API conta com apenas as rotas `/admin` e `/weather`

## Extração dos dados

Os dados desta API foram extraídos através do site: ``https://www.climatempo.com.br``

## Rota

A rota base da api está em: ``/weather``

## Inicando nossa Venv

Antes de iniciar nossa Aplicação, devemos instalar o virtual env através de: ``pip install virtualenv``

Após a instalação devemos criar uma venv, digitando o seguinte comando: ``virtualenv venv``

Para ativar nossa venv, devemos então rodar o próximo comando: ``.\venv\Scripts\activate`` se vc estiver em uma maquina Windows e ``source .\venv\Scripts\activate``

## Requerimentos do sistema

Todos os requerimentos do sistema serão instlados através do comando: ``pip install -r requirements.txt``

## Inicialização do sistema

Comando para inicialização do sistema: ``python .\manage.py runserver``