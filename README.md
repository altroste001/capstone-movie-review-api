# 🎬 Movie Review API (Django REST Framework)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Built with DRF](https://img.shields.io/badge/Built%20with-Django%20REST%20Framework-ff69b4.svg)](https://www.django-rest-framework.org/)

A robust **backend API** for managing movies and user-submitted reviews, built using **Django** and **Django REST Framework (DRF)**.

This project was developed as the **ALX Backend Engineering Capstone Project**.

---

## ✨ Core Features

The API provides core functionalities for movie listing, review submission, and secure administration.

### 🎥 Movies Management

* **Public Access:** List all movies and retrieve details.
* **Admin Access:** Exclusive endpoints for **creating, updating, and deleting** movie records.
* **Data Validation:**
    * Movie **Title** cannot be empty.
    * **Release Year** must be between 1800 and 2100.

### ⭐ Reviews System

* **Authenticated Submission:** Only **logged-in users** can create new reviews.
* **Ownership & Permissions:** Reviews can only be **updated or deleted by the original owner**.
* **Public Read:** All users can read all submitted reviews.
* **Data Validation:**
    * **Rating** must be an integer between **1 and 10**.
    * Reviews are linked to both **Movie** and **User** records.

### 🔐 Authentication

* **Current:** **Session-based authentication** is supported (via the DRF web UI).
* **Future:** Planned integration of **JWT (JSON Web Tokens)** for stateless API-level authentication.

---

## 🗄 Database Schema

The API's data structure is defined by these two core models, structured similarly to Django models.

### 🎥 Movie Model

```python
class Movie:
    title = CharField         # Movie title (Required)
    description = TextField   # Detailed plot summary
    release_year = IntegerField # Year of release (1800-2100)
    genre = CharField         # Genre of the film
```
⭐ Review Model
```python
class Review:
    movie = ForeignKey(Movie)   # Link to the Movie reviewed
    user = ForeignKey(User)     # Link to the User (reviewer)
    content = TextField         # Review text
    rating = IntegerField       # Rating from 1 to 10 (Validated)
    created_at = DateTimeField  # Timestamp of review creation
```
🚀 Installation & Setup
Follow these steps to set up and run the project locally.

Clone the Repository:
```bash
git clone [https://github.com/altroste001/capstone-movie-review-api.git](https://github.com/altroste001/capstone-movie-review-api.git)
cd capstone-movie-review-api
```
Create and Activate Virtual Environment:
Linux/macOS: 
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows (Command Prompt):
```bash
python -m venv venv
venv\Scripts\activate
```
Install Dependencies:
```bash
pip install -r requirements.txt
```
Run Migrations and Start Server:
```bash
python manage.py migrate
python manage.py runserver
```
The API server will be accessible at: http://127.0.0.1:8000/

📅 Project Timeline (Progress)

Week 1 : Project design, repository setup, and architecture planning.
Week 2 : Model implementation (Movie, Review) and initial CRUD endpoints for movies.
Week 3 : Review endpoints, user permissions, and initial data validation logic.
Week 4 : Documentation (README), permissions refinement, error handling, and testing.
Week 5 : Deployment to a hosting service (e.g., Render/Railway), PostgreSQL setup, final polish, and demo video.


👨‍💻 Author

Ayoub Bouabana Backend Engineering — ALX Capstone Project
