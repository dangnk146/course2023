# Project course

## Step 1: Create project 

    django-admin startproject course2023

## Step 2: Host postgresql

    docker-compose up

## Step 3: Code

    python -m pip install pandas
    python3 -m pip install python-pptx python-docx2pdf


# Run project

    python manage.py flush
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


    python manage.py startapp ...

# Data digram


<img src="./img/datadigram.png" />