FROM python:3.8.0-alpine

RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
WORKDIR /webapps
COPY requirements.txt /webapps/
ADD userTask /webapps/
RUN pip install --no-cache-dir -r /webapps/requirements.txt
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

CMD /bin/sh -c "python manage.py collectstatic --noinput \
                && python manage.py migrate --noinput \
                && gunicorn userTask.wsgi:application --bind 0.0.0.0:8000"
