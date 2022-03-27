# technical

Python 3.8 + Django 3.2 + Postgres 13

## Description

## Documentation

Use this template to start the backend development of your projects with Django

### Directory tree

```
├── apps
│   ├── orders
│   │   ├── fixtures
│   │   │   └── development.json
│   │   ├── management
│   │   │   ├── commands
│   │   │   │   ├── __init__.py
│   │   │   │   └── drivers.py
│   │   │   └── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── driver.py
│   │   │   └── order.py
│   │   ├── serializers
│   │   │   ├── __init__.py
│   │   │   ├── driver_serializer.py
│   │   │   └── order_serializer.py
│   │   ├── test
│   │   │   └── __init__.py
│   │   ├── views
│   │   │   ├── __init__.py
│   │   │   ├── driver_views.py
│   │   │   └── order_views.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   └── utils.py
│   └── __init__.py
├── htmlcov
├── technical
│   ├── settings
│   │   ├── partials
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── test.py
│   ├── static
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── dev-entrypoint.sh
│   ├── prod-entrypoint.sh
│   └── wait-for-it.sh
├── .coveragerc
├── .editorconfig
├── .envrc
├── .gitignore
├── Dockerfile
├── License
├── Makefile
├── README.md
├── docker-compose.override.yml
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── test-requirements.txt
```

### How to run the project ###

Before starting the project you must create your environment variables file (.env). [Here](https://gist.github.com/danialeresbar/617e55565ec89429c634bdfa46e885b9) is an example.

The project use docker, so just run:

```
docker-compose up
```

*Your app will run in url `localhost:8010`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```

To remove the docker containers including the database (Useful sometimes when dealing with migrations):

```
docker-compose down
```

> If you want to delete the information saved on docker volumes you can use `docker-compose down -v`

### Accessing Administration

The django admin site of the project can be accessed at `localhost:8010/admin`

By default, the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```

### Populate database with initial data

You can load information into the database by running the following command:

```
docker exec -it technical-web ./manage.py drivers
```

> There is a Makefile with abbreviations for useful project commands, if you have `make` installed you can use it 

### API

The API built has the autogenerated documentation of the drf-yasg package:

- redoc: `localhost:8010`
- swagger: `localhost:8010/swagger`

### Custom endpoints

#### `GET` api/v1.0/drivers/locate_driver/?query_parameters

- date: YYYY-MM-DD HH:MM
- lat: int
- lng: int

`api/v1.0/drivers/locate_driver/?date=2021-12-10T00:00:00.000Z&lat=35&lng=55`

#### `POST` api/v1.0/orders/schedule_order/


```json
{
  "date": "2022-04-05T16:00:00-00:00",
  "pickup_lat": 15,
  "pickup_lng": 65,
  "destination_lat": 35,
  "destination_lng": 25,
  "driver": 1
}
```

#### `GET` api/v1.0/orders/orders_by_date/?query_parameters

- date: YYYY-MM-DD

`api/v1.0/orders/orders_by_date/?date=2021-12-10`

#### `GET` api/v1.0/orders/orders_by_date/?query_parameters

- date: YYYY-MM-DD
- driver: int

`api/v1.0/orders/orders_by_driver_and_date/?date=2021-12-10&driver=1`
