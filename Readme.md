# Project course

## Step 1: Create project 

    django-admin startproject course2023

## Step 2: Host postgresql

    docker-compose up

## Step 3: Code

    python -m pip install pandas


# Run project

    python manage.py flush
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


    python manage.py startapp ...

# Data digram


<img src="./img/datadigram.png" />


# Push image to docker hub

    docker tag course2023master:local dangnguyensonia/course2023master
    docker build -t dangnguyensonia/course2023master:v3.0 .
    docker push dangnguyensonia/course2023master:v3.0


## Change to run database in docker
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'course',
            'USER': 'course',
            'PASSWORD': 'course',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }




-- Tạo user 'course' với mật khẩu 'course'
CREATE USER course WITH PASSWORD 'course';

-- Tạo database 'course' với chủ sở hữu là user 'course'
CREATE DATABASE course WITH OWNER = course;
