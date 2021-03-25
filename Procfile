release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb
migrate: bash deployment.sh
web: gunicorn CheeseBlog.wsgi --log-file -
