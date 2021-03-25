release: python manage.py migrate
migrate: bash deployment.sh
web: gunicorn CheeseBlog.wsgi --log-file -
