# mqtt-rest

REST API Server that handles MQTT Clients

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy mqtt_rest

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

# Simple Mosquitto broker

This is a simple [Mosquitto](https://mosquitto.org) broker to to quickly initialize projects requiring an MQTT broker. The config file is in the folder `config/mosquitto.conf`.

By default we activated the log and data persistance (respectively in `log` and `data` folder).
The authentication can be activated if needed.

# How to use

To start the container, just :

```
docker-compose -f broker.local.yaml up -d 
```

The Mosquitto broker is now available on localhost. You can test it easily (require Mosquitto client):

| In one shell:

```
mosquitto_sub -h localhost -t "sensor/temperature"
```

| In a second shell:

```
mosquitto_pub -h localhost -t sensor/temperature -m 23
```
