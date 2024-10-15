# FinTech Innovators API

## Overview

This project is a RESTful API built using Django and Django REST Framework (DRF) for FinTech Innovators, a startup focused on developing innovative payment processing solutions. The API handles secure and efficient transactions, with user authentication managed by JWT (JSON Web Tokens), and it integrates with PostgreSQL as the database. The project is deployed on AWS Elastic Beanstalk.

## Features

    - User Authentication: JWT-based authentication using Django REST Framework.
    - Transactions Management: Secure handling of user transactions.
    - PostgreSQL Integration: For robust data management and storage.
    - Deployment: Deployed on AWS Elastic Beanstalk.

## Requirements
    - Python 3.7+
    - Django 3.2+
    - PostgreSQL
    - AWS Elastic Beanstalk CLI (for deployment)

## Getting started

### 1. Clone the repository
```
git clone https://github.com/your-username/fintech-api.git
cd fintech-api
```
### 2. Set up a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up PostgreSQL
    1. Ensure PostgreSQL is installed and running.

    2. Create a PostgreSQL database and user:

    ```
    CREATE DATABASE fintech_db;
    CREATE USER fintech_user WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE fintech_db TO fintech_user;
    ```
### 5. Update Database Settings
In fintechapi/settings.py, update the database configuration to match your PostgreSQL setup:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fintech_db',
        'USER': 'fintech_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 6. Migrate the database
Run the following command to apply migrations:
```
python manage.py migrate
```
### 7. Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```
### 8. Run the development server
```
python manage.py runserver
```

Your server will be available at http://127.0.0.1:8000/.

# API Endpoints

## Authentication
    - Register: ```POST /auth/register/```
    Request body:
    ```
    {
        "username": "testuser",
        "password": "password123"
    }
    ```
    - Obtain JWT Token: POST /auth/api/token/
    Request body:

    ```
    {
        "username": "testuser",
        "password": "password123"
    }
    ```
    - Refresh Token: POST /auth/api/token/refresh/
    Request body:

    ```
    {
        "refresh": "your_refresh_token"
    }
    ```
## Transactions
- Create Transaction: POST /api/transactions/

(Requires JWT token in the Authorization header)

Request body:

```
{
  "amount": 100.00
}
```
- Get User's Transactions: GET /api/transactions/all/

(Requires JWT token in the Authorization header)

# Deployment to AWS Elastic Beanstalk

1. Install AWS Elastic Beanstalk CLI
```
pip install awsebcli
```
2. Initialize Elastic Beanstalk environment
Run the following command in your project directory:
```
eb init -p python-3.8 fintech-django-api
```
Choose the appropriate region and platform (Python 3.8+).

3. Create an Elastic Beanstalk environment and deploy
```
eb create fintech-env
eb deploy
```
4. Set environment variables
You will need to set your environment variables (such as database credentials) on AWS Elastic Beanstalk:

```
eb setenv DB_NAME=fintech_db DB_USER=fintech_user DB_PASSWORD=password DB_HOST=your-db-host
```
5. Monitor deployment
You can monitor the deployment logs with:

```
eb logs
```
6. Open the deployed application
After deployment, run:
```
eb open
```

# Screenshots
Login endpoint returning JWT token.


Creating a transaction with the user's JWT token.




