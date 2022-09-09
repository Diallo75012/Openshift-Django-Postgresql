# source : https://ruddra.com/deploy-django-to-openshift-3/
FROM python:3.8
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /app
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app

RUN pip install -r requirements.pip
RUN ./manage.py makemigrations
RUN ./manage.py migrate

# CMD gunicorn webApp.wsgi -b 0.0.0.0:8000
CMD gunicorn --env DJANGO_SETTINGS_MODULE=webApp.settings webApp.wsgi

EXPOSE 8000 22
