# Dockerfile
FROM python:3.8

# Install libffi-dev
RUN apt-get update && apt-get install -y libffi-dev

# Install libpq-dev (for PostgreSQL)
RUN apt-get install -y libpq-dev

# Install bash
RUN apt-get install -y bash

# Install other dependencies
RUN apt-get install -y build-essential zlib1g-dev libjpeg-dev

# Copy requirements.txt and install packages
COPY ./requirements.txt /app/requirements.txt

# Create a virtual environment and install dependencies
RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && /env/bin/pip install gunicorn \
    && /env/bin/pip install psycopg2-binary \
    && /env/bin/pip install psycopg2

# Copy the rest of the application code
COPY . /app
WORKDIR /app

# Set environment variables
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["bash", "-c", "/env/bin/python manage.py collectstatic --noinput && gunicorn --bind :8000 --workers 3 course2023.wsgi"]
