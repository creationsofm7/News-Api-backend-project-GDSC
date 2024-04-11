# News API Backend Project

This project is a backend service for a News API. It is designed to provide news data to frontend applications.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Django 5.0.8
- Django Rest Framework

You can install these packages using pip:

```sh
pip install python==3.8.10 django==5.2.8 djangorestframework==3.12.4
```

### Installing

1. Clone the repository:

```sh
git clone
```

2. Navigate to the project directory:

```sh
cd news-api-backend
```

3. create a virtual environment:

```sh
python -m venv venv
```

4. Activate the virtual environment:

```sh
source venv/bin/activate
```

5. Install the project dependencies:

```sh
pip install -r requirements.txt
```

6. Apply the database migrations:

```sh
python manage.py migrate
```


7. Run the development server:

```sh
python manage.py runserver
```

The development server should now be running at http://
localhost:8000.

## API Endpoints

The following endpoints are available:

- `/api/posts/` - GET: Get all news articles
- `/api/posts/<int:pk>/` - GET: Get a single news article
- `/api/posts/<int:pk>/` - PUT: Update a news article
- `/api/posts/<int:pk>/` - DELETE: Delete a news article
- `/api/comments/` - POST: Create a new news article
- `/api/comments/<int:pk>/` - GET: Get all comments for a news article
- `/api/comments/<int:pk>/` - POST: Create a new comment for a news article
- `/api/comments/<int:pk>/` - PUT: Update a comment
- `/api/comments/<int:pk>/` - DELETE: Delete a comment

## Built With

- [Django](https://www.djangoproject.com) - The web framework used
- [Django Rest Framework](https://www.django-rest-framework.org) - The REST API framework used








