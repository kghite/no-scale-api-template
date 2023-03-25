# Project-scale Deployable Flask API

An over-featured API template to provide low-cost, cloud-based backend functionality for Raspberry Pi projects.

Features:

* Docker development and Compose production builds
* Unit testing with Pytest
* Low-user authorization with API keys (manually added)
* Linting and formatting with Black and Flake8
* Payload validation with Pydantic
* Custom error handling
* ~~SQLAlchemy database~~

## Develop workflow

The development workflow commands are aliased in the [Makefile](Makefile).


1) Install development dependencies

        make devel-install

2) Create and populate a `.env` file based on .env.template

        cp .env.template .env

   The USER_API_KEY is required to access any restricted endpoints in this application. A user API key can be generated 
   with `uuid-gen` and then provided to the Raspberry Pi frontend node(s).  Keys to access any external APIs should also be added via `.env`.


3) Lint and reformat any new code

         make format          # Reformats all code

         make format-check    # Reports issues but doesn't auto-format

4) Run tests with Pytest

         make test

      The pytest configuration is specified and can be updated in `tests/pytest.ini`.


5) Build and run the API image

         make devel-build

         make devel-run

   This kicks off a multi-stage docker build to create a pared down final image running a Gunicorn server.

## Deploy workflow

**TODO**

`docker compose up`
