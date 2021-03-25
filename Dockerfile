FROM python:3-slim

RUN apt-get update && apt-get install -y gcc && pip install flask uwsgi

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

EXPOSE 8000

RUN useradd uwsgi && chown -R uwsgi /smash
USER uwsgi

CMD [ "uwsgi", "smash-py.ini" ]
