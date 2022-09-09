#!/bin/bash

python3 manage.py migrate
python3 manage.py runserver

#exec mod_wsgi-express start-server $ARGS wsgi/application