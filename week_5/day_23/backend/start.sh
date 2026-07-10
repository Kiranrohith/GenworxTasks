#!/bin/sh

echo "=================================="
echo "Waiting for PostgreSQL..."
echo "=================================="

until pg_isready -h postgres -p 5432 -U postgres
do
    echo "PostgreSQL is unavailable - sleeping..."
    sleep 2
done

echo "=================================="
echo "PostgreSQL is ready!"
echo "=================================="

echo "Running Alembic migrations..."

alembic upgrade head

echo "=================================="
echo "Starting FastAPI..."
echo "=================================="

exec uvicorn app.main:app --host 0.0.0.0 --port 8000