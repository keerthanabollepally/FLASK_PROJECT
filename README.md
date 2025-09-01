# Flask User Management API

A simple Flask project that provides user **register**, **login** (using JWT), and **profile operations**.

---

## Features

- Uses Flask and SQLAlchemy (SQLite as the database)
- User passwords are stored securely (hashed)
- Authentication using JWT tokens (`flask-jwt-extended`)
- Modular project with routes separated in files (blueprints)
- Examples included for testing with Postman and curl
- Configuration via `.env` file for keys and database URL

---

## Project Structure
flask_user_api/
├── app.py              # Main Flask application
├── models.py           # Database models
├── database.py         # Database setup
├── routes/
│   ├── auth.py         # Register and login routes
│   └── user.py         # User profile routes (view, update, delete)
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (secret key, DB)
└── README.md


---

## Setup

1. Create and activate a virtual environment:

      - python -m venv .venv

      - Windows:
         .venv\Scripts\activate

      - Mac/Linux:
         source.venv/bin/activate


2. Install required packages:
   pip install -r requirements.txt


3. Create `.env` file with your settings:

JWT_SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///db.sqlite


---

## Running the App

python app.py



The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## API Endpoints and Usage

### Register New User

- **POST** `/api/v1/auth/register`

Request body example:

{
"name": "Keerthana",
"email": "keer@example.com",
"password": "secret123"
}


---

### Login User

- **POST** `/api/v1/auth/login`

Request body example:

{
"email": "keer@example.com",
"password": "secret123"
}


Response contains an `access_token` to use in later requests.

---

### Get User Profile

- **GET** `/api/v1/users/me`

Headers:

Authorization: Bearer <access_token>


---

### Update Profile

- **PUT** `/api/v1/users/me`

Headers:

Authorization: Bearer <access_token>


Request body example:

{
"name": "Keerthana B.",
"password": "newsecret123"
}


---

### Delete Account

- **DELETE** `/api/v1/users/me`

Headers:

Authorization: Bearer <access_token>

---

## Testing with curl

### Register (Linux/Mac)

curl -X POST http://127.0.0.1:5000/api/v1/auth/register
-H "Content-Type: application/json"
-d '{"name":"Keerthana","email":"keer@example.com","password":"secret123"}'



### Login (Linux/Mac)

curl -X POST http://127.0.0.1:5000/api/v1/auth/login
-H "Content-Type: application/json"
-d '{"email":"keer@example.com","password":"secret123"}'


Use the `access_token` from login response for protected routes.

---

## Notes

- Change `JWT_SECRET_KEY` in `.env` for security purposes.
- Use PostgreSQL or MySQL by changing `DATABASE_URL` in `.env` if needed.
- Feel free to add more resources (e.g., to-do list, notes) by creating new routes.
