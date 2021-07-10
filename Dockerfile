FROM python:3-slim

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

RUN apt-get update && apt-get install -y gcc
ENV VIRTUAL_ENV=/smash/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

RUN useradd uwsgi && chown -R uwsgi /smash
USER uwsgi
RUN pip install --no-cache-dir flask uwsgi

CMD [ "uwsgi", "smash-py.ini" ]
