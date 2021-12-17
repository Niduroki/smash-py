FROM python:3-alpine

RUN apk add --no-cache gcc libc-dev linux-headers

RUN mkdir /smash/
WORKDIR /smash/
COPY . /smash/

ENV VIRTUAL_ENV=/smash/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

RUN adduser -S uwsgi && chown -R uwsgi /smash
USER uwsgi
RUN pip install --no-cache-dir flask uwsgi

CMD [ "uwsgi", "smash-py.ini" ]
