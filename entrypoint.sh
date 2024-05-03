if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    wait-for-it $SQL_HOST:$SQL_PORT -t 30
    echo "PostgreSQL started"
    python manage.py collectstatic --noinput
    gunicorn --bind 0.0.0.0:8000 mebel.wsgi
fi


exec "$@"