***********************
Introduction & Settings
***********************

Introduction
============

Photo Voting is a simple API built with django restframework.
It demonstrate how to build a Backend API with the following features:
1. user registeration
2. authenticating with tokens
3. image endpoints
4. voting on images
5. unit testing APIs

There is an `ionic <https://github.com/TheBlackDude/photo_voting_client/>`__ application to test it with.
Go to the `repo <https://github.com/TheBlackDude/photo_voting_client/>` to see how to configure it.

Setup
=====

No local setup should be needed apart from:
- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__


creating a .env file with the following Environment variables.

.. code:: bash
    DEBUG=whatever
    SECRET_KEY=whatever
    PG_USERNAME=whatever
    PG_PASSWORD=whatever
    PG_NAME=whatever
    PG_HOST=whatever
    PG_PORT=5432 (default postgres port)

The local dev setup uses **docker-compose** to spin up all necessary services.
Make sure you have it installed and can connect to the **docker daemon**.

Build the app
-------------

Run in project directory after you clone the repository:

.. code:: bash

    docker-compose build

Run the tests (there is a few, just to show an example)
-------------

Type command below to run tests:

.. code:: bash

    docker-compose run voting manage createsuperuser

Run the app
===========

Start the dev server
------------------

Run in project directory:

.. code:: bash

    docker-compose up

This will build and download the containers and start them. The ``docker-compose.yml``
file describes the setup of the containers.

The API docs should be reachable at ``http://localhost:8000/api/v1/docs/``.

Create a user
-------------

To create a superuser type:

.. code:: bash

    docker-compose run voting manage createsuperuser


Run commands on the server
==========================

Each docker container uses the same script as entrypoint. The ``entrypoint.sh``
script offers a range of commands to start services or run commands.
The full list of commands can be seen in the script.
The pattern to run a command is always
``docker-compose run <container-name> <entrypoint-command> <...args>``

The following are some examples:

+-------------------------------------+----------------------------------------------------------+
| Action                              | Command                                                  |
+=====================================+==========================================================+
| Run tests                           | ``docker-compose run genecare test``                     |
+-------------------------------------+----------------------------------------------------------+
| Run django commands                 | ``docker-compose run genecare manage help``              |
+-------------------------------------+----------------------------------------------------------+
| Create a django shell               | ``docker-compose run genecare manage shell``             |
+-------------------------------------+----------------------------------------------------------+
| Show ORM migrations                 | ``docker-compose run genecare manage showmigrations``    |
+-------------------------------------+----------------------------------------------------------+


Containers and services
=======================

These are the two containers we have at the moment.

+-----------+-------------------------------------------------------------------------+
| Container | Description                                                             |
+===========+=========================================================================+
| voting  | `Django <https://www.djangoproject.com/>`__                             |
+-----------+-------------------------------------------------------------------------+
| db        | `PostgreSQL <https://www.postgresql.org/>`__ database                   |
+-----------+-------------------------------------------------------------------------+

All of the container definitions for development can be found in the ``docker-compose.yml``.

.. note:: Postgresql uses Django ORM models for table configuration and migrations.
