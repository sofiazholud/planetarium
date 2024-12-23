# Planetarium API

API service for managing planetarium sessions, reservations, and astronomy shows, written with Django Rest Framework (DRF).

## Installing using GitHub

### Prerequisites

1. Install PostgreSQL and create a database.
2. Make sure Python 3.9+ is installed on your system.

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/sofiazholud/planetarium.git


### Navigate to the project directory:
cd ..

### Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate (On Windows: venv\Scripts\activate)

### Install the required dependencies:
pip install -r requirements.txt

### Set up environment variables for your database and secret key:
set DB_HOST=<your-db-hostname>
set DB_NAME=<your-db-name>
set DB_USER=<your-db-username>
set DB_PASSWORD=<your-db-password>
set SECRET_KEY=<your-secret-key>

### Apply database migrations:
python manage.py migrate

### Create a superuser to access the admin panel (optional):
python manage.py createsuperuser

### Start the development server:
python manage.py runserver

### Run the tests using the following command:
python manage.py test

### Run with docker
Docker should be installed

docker-compose build
docker-compose up

### Getting access
 - create user via/api/user/register
 - get access token via api/user/token


### API Endpoints
Astronomy Shows: /api/astronomy_shows/
Show Sessions: /api/show_sessions/
Reservations: /api/reservations/
Planetarium Domes: /api/planetarium_domes/
For a full list of endpoints, visit /api/ while the server is running.

### Features
Manage astronomy shows and planetarium domes.
Create, list, and manage show sessions.
User authentication and reservations for show sessions.
Token-based authentication using SimpleJWT.
Contributing
Feel free to submit issues or pull requests to improve the project.

