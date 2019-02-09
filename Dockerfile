FROM python:3.6

RUN pip install flask uwsgi

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

EXPOSE 80

CMD [ "uwsgi", "smash-py.ini" ]
