FROM python:3-slim

RUN apt-get update && apt-get install -y gcc && pip install flask uwsgi

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

EXPOSE 80

RUN useradd smash && chown -R smash /smash
USER smash

CMD [ "uwsgi", "smash-py.ini" ]
