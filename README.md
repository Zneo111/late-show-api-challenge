# Late Show API

A Flask REST API for managing a Late Night TV show system.

---

##  Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/Zneo111/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. **Install Dependencies**

```bash
pipenv install
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv
pipenv shell
```

### 3. **PostgreSQL Setup**

- Ensure PostgreSQL is running.
- Create the database:

```sql
CREATE DATABASE late_show_db;
```

### 4. **Configure Environment**

Edit `server/config.py` and set:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
JWT_SECRET_KEY = "<your_jwt_secret>"
```
Replace `<user>`, `<password>`, and `<your_jwt_secret>` with your actual values.

---

##  How to Run

### 1. **Database Migration**

```bash
export FLASK_APP=server/app.py
flask db init         
flask db migrate -m "initial migration"
flask db upgrade
```

### 2. **Seed the Database**

```bash
python server/seed.py
```

### 3. **Start the Server**

```bash
flask run
# or
python server/app.py
```

---

##  Authentication Flow

- **Register:** `POST /register` with JSON `{ "username": "...", "password": "..." }`
- **Login:** `POST /login` with JSON `{ "username": "...", "password": "..." }`
- **Receive JWT:** Use the returned token for protected routes.
- **Protected Endpoints:**  
  Add header: `Authorization: Bearer <your_token>`

---


### Sample: Register

```http
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```

### Sample: Login

```http
POST /login
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```

**Response:**
```json
{
  "access_token": "<JWT_TOKEN>"
}
```

### Sample: Protected Route

```http
POST /appearances
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "guest_id": 1,
  "episode_id": 1,
  "rating": 5
}
```

---

##  Postman Usage Guide

1. Open Postman (or the VS Code Postman extension).
2. Import `challenge-4-lateshow.postman_collection.json` from the project root.
3. Use the collection to test all endpoints.
4. For protected routes, log in first and use the returned JWT token in the `Authorization` header.

---

## Notes

- All models and routes follow the MVC pattern.
- PostgreSQL is required (no SQLite).
- JWT authentication is enforced on protected routes.
- Seed data is provided for quick testing.

---

## ✅ Submission Checklist

- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and have been tested in Postman
- [x] Clean, complete README.md
- [x] Postman collection included
- [x] GitHub repo pushed and shared

---

Feel free to share this README with anyone who needs to set up or use your Late Show API!
