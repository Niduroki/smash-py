FROM python:3.7-slim

RUN apt-get update && apt-get install -y gcc && pip install flask uwsgi

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

EXPOSE 80

CMD [ "uwsgi", "smash-py.ini" ]
