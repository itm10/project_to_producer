FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput


RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/app/entrypoint.sh"]