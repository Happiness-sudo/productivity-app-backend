# Productivity App Backend (Flask API)

Project Description

This is a simple Flask backend API for a productivity app where users can create and manage their personal notes.
The application includes user authentication using JWT and ensures that each user can only access their own data.

---

Installation Instructions

1. Clone the repository:

```
git clone https://github.com/Happiness-sudo/productivity-app-backend.git
cd productivity-app-backend
```

2. Install dependencies:

```
pipenv install
```

3. Activate virtual environment:

```
pipenv shell
```

4. Set environment variable:

```
export FLASK_APP="app:create_app"
```

5. Run database migrations:

```
flask db upgrade
```

---

 Run the Application

```
flask run
```

Server will run on:

```
http://127.0.0.1:5000
```

---

## Authentication

This API uses JWT authentication.

After login, include the token in requests:

```
```

---

API Endpoints
 Auth Routes

**POST /signup**

* Create a new user
* Body:

```
{
  "username": "yourname",
  "password": "yourpassword"
}
```

---

POST /login

 Login user and receive JWT token


GET /me

 Get current logged-in user
 Requires token

---

### Notes Routes

GET /notes?page=1

 Get all notes for logged-in user (paginated)

---

**POST /notes**

* Create a new note
* Body:

```
{
  "title": "Note title",
  "content": "Note content"
}
```

---

**PATCH /notes/<id>**

* Update a note

---

**DELETE /notes/<id>**

* Delete a note


 Seed Data

To populate the database with sample data:

python seed.py


Features

* User signup and login
* Password hashing using bcrypt
* JWT authentication
* Protected routes
* User-specific data (notes)
* Full CRUD operations
* Pagination support


 Tech Stack

* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* Flask-Bcrypt
* SQLite

---

Notes

* Each user can only access their own notes
* Unauthorized access is blocked
* API returns JSON responses


