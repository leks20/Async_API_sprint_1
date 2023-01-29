# Проектная работа четвёртого спринта

## TEAM_22:
[do8rolyuboff](https://github.com/do8rolyuboff) [leks20](https://github.com/leks20) [denischenc](https://github.com/denischenc)

## Что было сделано:
Запуск микросервиса, базы, etl, elasticsearch чрезе docker-compose

Созданы pydantic модели: `film`, `genre` и `person`

Добавлены новые ETL пайплайны для `genre`, `person` и доработал пайплан для `film`.

Реализован сервис для получения информации из Elasticsearch по id и полнотектовый поиск для каждой из моделей(fiml/genre/person).

Сделано кешировнаие каждой ручки.


## Запуск проекта:

Создать и заполнить в корневой директории и директории etl4 `.env` файл по шаблону example.env

`cmd: docker-compose up --build`

В течение ~1 минуты, заполнится база и etl перенесет данные в elasticsearch.

## Swagger:
http://localhost:8006/api/openapi#/
