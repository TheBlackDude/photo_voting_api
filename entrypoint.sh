#!/bin/bash
set -e

show_help() {
  echo """
  Commands
  -----------------------------------------
  start_dev      : start the django dev server
  test           : run unit tests
  fix            : fix linting errors
  manage         : run django commands
  """
}

export PYTHONPATH="/code/:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE=config.settings

case "$1" in
  "start_dev" )
    # run migrations first if theres any && start the dev server
    ./manage.py migrate --noinput
    ./manage.py runserver 0.0.0.0:8000
  ;;
  "test" )
    # linting first
    flake8 ./
    # run python tests and pass on any args e.g individual tests
    ./manage.py test "${@:2}"
  ;;
  "fix" )
    # fix all linting errors automagically
    autopep8 --in-place -a -a -r ./
  ;;
  "manage" )
    # run django commands
    ./manage.py "${@:2}"
  ;;
  * )
    show_help
  ;;
esac
