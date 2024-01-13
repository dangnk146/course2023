# Cách biên dịch
### Step1: Cài đặt cho python các package cần thiết

    pip install -r requirements.txt

Nếu gặp lỗi có thể thực hiện 1 trong 2 cách sau

    python -m pip install -r requirements.txt
    python3 -m pip install -r requirements.txt

### Step2: Cài đặt docker - container

    https://docs.docker.com/desktop/install/windows-install/

### Step3: Khởi động database

    cd course2023
    docker-compose up

### Step4: Tạo các record cho database

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

<i>Note: Super users need to be role a teacher. Though the user has role admin access in django admin, the user does not access the login in manage class Dashboard without no role teacher. Finally, the user needs two role teacher and supper admin if the user wants to access Dash board manage admin.</i>

# Chạy chương trình

    python manage.py runserver