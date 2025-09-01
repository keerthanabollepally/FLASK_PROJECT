# 🔒 Flask User Management API

A simple and secure Flask API for managing user accounts, including **registration**, **login** with **JWT authentication**, and basic **profile management** operations.

-----

## ✨ Features

  * **Frameworks**: Built with **Flask** and **SQLAlchemy** (using SQLite as the default database).
  * **Security**: User passwords are **hashed** using a secure cryptographic algorithm.
  * **Authentication**: Uses **JSON Web Tokens (JWT)** for stateless authentication with `flask-jwt-extended`.
  * **Modularity**: Project routes are organized into separate files using **Flask Blueprints** for a clean, scalable structure.
  * **Configuration**: All sensitive data, such as the secret key and database URL, is managed through a `.env` file.
  * **Documentation**: Includes examples for API usage with Postman and `curl`.

-----

## 📂 Project Structure

```
flask_user_api/
├── app.py             # Main Flask application entry point
├── models.py          # Database models (User)
├── database.py        # Database setup and session management
├── routes/
│   ├── auth.py        # Routes for user registration and login
│   └── user.py        # Routes for authenticated user profile operations (get, update, delete)
├── requirements.txt   # Python dependencies
├── .env               # Environment variables for configuration
└── README.md
```

-----

## 🚀 Setup

1.  **Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On Mac/Linux:
    source .venv/bin/activate
    ```

2.  **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Create your `.env` file**:
    Create a file named `.env` in the root directory and add your configuration settings.

    ```env
    JWT_SECRET_KEY=your_super_secret_key_here
    DATABASE_URL=sqlite:///db.sqlite
    ```

-----

## ▶️ Running the App

To start the development server, run the main application file:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`.

-----

## 📝 API Endpoints and Usage

### Register New User

  * **Endpoint**: `POST /api/v1/auth/register`
  * **Body**:
    ```json
    {
      "name": "Keerthana",
      "email": "keer@example.com",
      "password": "secret123"
    }
    ```
<img width="1913" height="936" alt="Screenshot 2025-09-01 212913" src="https://github.com/user-attachments/assets/c06a9415-fcc0-4be5-a86a-d62cbbfc8763" />

### Login User

  * **Endpoint**: `POST /api/v1/auth/login`
  * **Body**:
    ```json
    {
      "email": "keer@example.com",
      "password": "secret123"
    }
    ```
  * **Response**: A successful login returns a **JWT access token**. You must include this token in the headers of all subsequent requests to protected endpoints.

### Get User Profile

  * **Endpoint**: `GET /api/v1/users/me`
  * **Headers**:
    ```
    Authorization: Bearer <access_token>
    ```

### Update Profile

  * **Endpoint**: `PUT /api/v1/users/me`
  * **Headers**:
    ```
    Authorization: Bearer <access_token>
    ```
  * **Body**:
    ```json
    {
      "name": "Keerthana B.",
      "password": "newsecret123"
    }
    ```
    <img width="1911" height="972" alt="Screenshot 2025-09-01 213009" src="https://github.com/user-attachments/assets/d754e082-2de0-48a8-9e2e-f4d295516263" />

<img width="1909" height="908" alt="Screenshot 2025-09-01 213019" src="https://github.com/user-attachments/assets/e97850e1-9967-4598-bcc9-29cd2e6fc036" />


### Delete Account

  * **Endpoint**: `DELETE /api/v1/users/me`
  * **Headers**:
    ```
    Authorization: Bearer <access_token>
    ```

-----
<img width="1919" height="1000" alt="Screenshot 2025-09-01 213034" src="https://github.com/user-attachments/assets/e3f50d21-cfa9-401c-b413-4645348b348e" />


## 💻 Testing with `curl`

Here are some examples for testing the API from your terminal.

#### Register a New User

```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/register \
-H "Content-Type: application/json" \
-d '{"name":"Keerthana","email":"keer@example.com","password":"secret123"}'
```

#### Login

```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"keer@example.com","password":"secret123"}'
```

After logging in, copy the `access_token` from the response to use in authenticated requests.

-----

## ⚠️ Notes

  * Remember to change the `JWT_SECRET_KEY` in your `.env` file for production to ensure security.
  * To use a different database like **PostgreSQL** or **MySQL**, simply change the `DATABASE_URL` in the `.env` file and install the corresponding driver (e.g., `psycopg2` for PostgreSQL).
  * The modular structure makes it easy to add new features. You can create new blueprint files in the `routes/` directory to manage additional resources like notes, blog posts, or to-do lists.
