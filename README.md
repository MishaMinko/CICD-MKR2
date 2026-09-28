# CICD-MKR2

Modular Assessment (MA) for the **CI/CD** course. Implements a Django web application for managing recipes organized by category, with automated testing configured via GitHub Actions.

The project was completed as a modular assignment for the CI/CD course — a practical task involving the creation of a Django application followed by the automation of testing via a CI pipeline (GitHub Actions), which is a fundamental element of the continuous integration (CI) process.

## Technology Stack

- **Python**
- **Django** — web framework
- **SQLite** — database (for development)
- **PostgreSQL** — test database in the CI pipeline
- **GitHub Actions** — automated test execution

## Functionality

- View the list of recipes
- View recipes by category
- Django admin panel for managing recipes and categories

## Project structure

```
project_recipes/          # Django project settings
├── settings.py
├── urls.py
└── wsgi.py / asgi.py

recipes/                  # main application
├── models.py              # Recipe and Category models
├── views.py                # page views
├── admin.py                # registering models in the admin interface
├── urls.py
├── migrations/             # database migrations
└── templates/               # HTML templates (main.html, category_list.html)

templates/base.html       # base template
manage.py                 # Django entry point
.yaml                     # CI pipeline configuration (GitHub Actions)
```

## How to start project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Apply migrations:

```bash
python manage.py migrate
```

3. Start the development server:

```bash
python manage.py runserver
```

4. Open the following URL in your browser: `http://127.0.0.1:8000`

## Testing

The CI pipeline automatically sets up the PostgreSQL test database, applies migrations, and runs Django tests with every push or pull request:

```bash
python manage.py test
```
