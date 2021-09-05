FROM python:3.8.5

WORKDIR /code

COPY . /code

RUN pip3 install -r /code/requirements.txt

CMD gunicorn phonebookapi.wsgi:application --bind 0.0.0.0:8000