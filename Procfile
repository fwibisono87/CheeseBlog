release 1: python manage.py makemigrations
release 2: python manage.py migrate --run-syncdb
migrate: bash deployment.sh
web: gunicorn CheeseBlog.wsgi --log-file -
