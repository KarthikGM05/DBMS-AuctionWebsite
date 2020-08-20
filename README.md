# Auction Website using Django and PostgreSQL

## Installation

Requires python 3.6 or higher. Clone the repo, install virtualenv (if you haven't already) and create a new virtual environment. Activate the virtual environment.

```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

Install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

## Connecting to PostgreSQL

You can see the following lines in auctionsonline\auctionsonline\settings.py

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djauction',
        'HOST': 'localhost',
        'PASSWORD': 'postgres',
        'USER': 'postgres',
        'PORT': '5432',
    }
}
```

This instructs Django to connect to a postgres database named 'djauction' on the given host and port using the username and password given. Edit this to match your postgres username and password. Create a new postgres database 'djauction' or change the name as you'd like.

## Migrating the database

Currently, migrations are up to date with the models. If you make any changes to the models, then run both of the following command to create migrations and migrate them to the database. If you haven't made any changes, just run the latter command.

```bash
manage.py makemigrations
manage.py migrate
```

## Running the app

Just run,

```bash
python manage.py runserver
```

and you'll see the server has started. Follow the link to view the app on your browser.
