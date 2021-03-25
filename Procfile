release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb
migrate: bash deployment.sh
web: python manage.py collectstatic --no-input; gunicorn myapp.wsgi --log-file - --log-level debug
web: gunicorn CheeseBlog.wsgi --log-file -

