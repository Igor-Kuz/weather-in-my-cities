# Weather-in-my-cities
[![Build Status](https://app.travis-ci.com/Igor-Kuz/weather-in-my-cities.svg?branch=master)](https://app.travis-ci.com/Igor-Kuz/weather-in-my-cities)

## App which shows the weather in different cities according to info from openweathermap API In addition to the current temperature, the user is provided with information about
- in which country the selected city is located,
- information about the geographical coordinates of the settlement,
- air humidity,
- wind speed and direction,
- geographic coordinates and clouds.

 The application is built on top of the Django framework using the requests library.
 
 ## Приложение которое отображает метеорологические данные в населённом пункте который задал пользователь, согласно информации полученной от openweathermap API. Пользоватю доступно получение информации о погоде в нескольких городах сразу. Кроме текущей температуры пользователю предоставляется информация о том:
- в какой стране расположен выбранный город,
- информация о географических координатах населенного пункта,
- влажности воздуха,
- скорости и направлении ветра,
- географических координатах и облачности.
Приложение создано на базе фреймворка Django с использованием библиотеки requests.


### Инструменты разработки
 
**Стек:**

 - Python >= 3.7

- Django >= 3

- requests >= 2.23.0

- sqlite3


## Установка и запуск

##### 1) Открыть терминал или консоль и перейти в нужную Вам директорию

##### 2) Клонировать репозиторий и поставить звездочку)

    git clone https://github.com/Igor-Kuz/weather-in-my-cities.git

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение


##### 4 ) Устанавливить зависимости:

    pip install -r reqirements.txt

##### 5) Выполнить миграции

##### 6) Запустить сервер

    python manage.py runserver