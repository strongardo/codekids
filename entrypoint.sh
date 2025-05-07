#!/bin/sh

set -e  # Прерывать выполнение скрипта при ошибке

echo "Ожидание PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.5
done
echo "PostgreSQL готов"

echo "Применяем миграции..."
python manage.py migrate

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Запуск Gunicorn..."
exec gunicorn codekids.wsgi:application --bind 0.0.0.0:8000
