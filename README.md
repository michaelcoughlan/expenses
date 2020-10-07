# expenses

## Prerequisites
    - Docker

## Scaffolding the project

```bash
    $ docker-compose run web django-admin startproject expenses .
```

## Getting the project started

```bash
    # Run database migrations
    $ docker-compose run web python manage.py migrate

    # Start the environment
    $ docker-compose up
```
