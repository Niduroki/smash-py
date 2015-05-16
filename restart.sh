source ../venv/bin/activate # required to use virtualenv?
kill -9 `cat smash-py.pid`
uwsgi smash-py.ini
