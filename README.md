    Movie Review API

A backend API built with Django and Django REST Framework for managing movie reviews.
This project is developed as part of the ALX Backend Engineering Capstone Project.

    Project Overview

The Movie Review API allows users to:

Create movie reviews

View all reviews

Retrieve individual reviews

Update reviews

Delete reviews

The API is designed following REST principles and will later include authentication, permissions, and filtering.

    Tech Stack

Python 3

Django 5+

Django REST Framework

SQLite / PostgreSQL (depending on deployment)

    Features (Week 3)

Django project setup

Review model

CRUD endpoints

DRF testing interface

Clean and modular project structure

    Installation & Setup

Clone the repository:

git clone https://github.com/altroste001/capstone-movie-review-api.git
cd capstone-movie-review-api


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver

    API Endpoints (Week 3)
Method	Endpoint	Description
GET	/api/reviews/	List all reviews
POST	/api/reviews/	Create a new review
GET	/api/reviews/<id>/	Retrieve a specific review
PUT	/api/reviews/<id>/	Update a review
DELETE	/api/reviews/<id>/	Delete a review

    Next Steps (Week 4)

Add authentication

Add permissions (only owner updates/deletes)

Add search & filtering

Add pagination

Add error handling and validations

    Author

Ayoub Bouabana
Backend Engineering Student — ALX Program

    License

This project is for educational purposes under the ALX Capstone Program.
