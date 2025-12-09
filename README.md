🎬 Movie Review API (DRF)

A backend API built using Django and Django REST Framework that allows users to browse movies, submit reviews, and interact with authenticated endpoints.

This project is developed as part of the ALX Backend Engineering Capstone Project.

🚀 Project Features (Completed So Far)
🎥 Movies

List all movies

Get movie details

Admin-only: create, update, delete movies

Validation:

Title cannot be empty

Release year must be between 1800–2100

⭐ Reviews

Authenticated users can add reviews

Only the review owner can update/delete

Public users can read all reviews

Rating must be between 1–10

Review is linked to both Movie and User

🔐 Authentication

Session-based authentication supported in the DRF UI

Future: JWT for API-level auth (Week 5 optional)

🧱 Tech Stack
Technology	Purpose
Python	Main language
Django	Backend framework
Django REST Framework	API layer
SQLite	Development database
Admin Panel	Movie & review management
🗄 Database Models
Movie
Field	Type
title	CharField
description	TextField
release_year	IntegerField
genre	CharField
Review
Field	Type
movie	ForeignKey → Movie
user	ForeignKey → User
content	TextField
rating	IntegerField (1–10)
created_at	DateTime
🔗 API Endpoints
🎥 Movies
Method	Endpoint	Description	Permissions
GET	/api/movies/	List all movies	Public
POST	/api/movies/	Create movie	Admin only
GET	/api/movies/<id>/	Movie details	Public
PUT/PATCH	/api/movies/<id>/	Update movie	Admin only
DELETE	/api/movies/<id>/	Delete movie	Admin only
⭐ Reviews
Method	Endpoint	Description	Permissions
GET	/api/reviews/	List all reviews	Public
POST	/api/reviews/	Create review	Authenticated
GET	/api/reviews/<id>/	Review detail	Public
PUT/PATCH	/api/reviews/<id>/	Update review	Owner only
DELETE	/api/reviews/<id>/	Delete review	Owner only
⚙️ Installation & Setup
git clone https://github.com/altroste001/capstone-movie-review-api
cd capstone-movie-review-api

python -m venv venv
venv\Scripts\activate   

   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

📅 Project Timeline (Progress)
Week 1 – Planning

✔ Project design, repo setup, architecture planning

Week 2 – Models & CRUD

✔ Movie model
✔ Review model
✔ Endpoints for movies

Week 3 – Auth & Permissions

✔ Review endpoints
✔ User restrictions
✔ Data validation

Week 4 – Documentation & Cleanup

✔ README
✔ Permissions
✔ Validation
✔ Error handling
✔ Testing endpoints

Week 5 – Deployment (Upcoming)

🔜 Deploy to Render/Railway
🔜 PostgreSQL setup
🔜 Final polishing
🔜 Demo video

👨‍💻 Author

Ayoub Bouabana
Backend Engineering — ALX
