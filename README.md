Late Show API Code Challenge
=============================

This project implements a RESTful API for managing a late-night talk show database, including users, guests, episodes, and appearances. Built with Flask, PostgreSQL, and JWT authentication, it provides endpoints for user registration/login, guest and episode management, and appearance ratings. The project is developed in a Windows Subsystem for Linux (WSL) environment (Ubuntu) and tested with Postman.

Features
--------

- **User Authentication**: Register and login with JWT-based authentication.
- **Guest Management**: Retrieve guest information.
- **Episode Management**: List episodes with details.
- **Appearance Management**: Create and rate guest appearances on episodes.
- **Database**: PostgreSQL with SQLAlchemy and Flask-Migrate for schema management.
- **Testing**: Postman collection for endpoint validation.

Prerequisites
-------------

- **WSL** (Ubuntu 20.04 or later recommended).
- **Python** 3.8+.
- **PostgreSQL** 15+.
- **Postman** for API testing.
- **VS Code** (optional, for development).
- **pip** and **virtualenv** for Python package management.

Project Structure
-----------------

```
late-show-api-challenge/
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── controllers/
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   ├── auth_controller.py
│   ├── models/
│       ├── user.py
│       ├── guest.py
│       ├── episode.py
│       ├── appearance.py
├── migrations/
├── seed.py
├── challenge-4-lateshow.postman_collection.json
├── README.md
```

Setup Instructions
------------------

### 1. Clone the Repository

```bash
git clone <repository-url>
cd late-show-api-challenge
```

### 2. Install PostgreSQL in WSL

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
```

Verify PostgreSQL is running on port 5432:

```bash
sudo service postgresql status
```

### 3. Configure PostgreSQL User

Set a password for the postgres user:

```bash
sudo -u postgres psql
\password postgres
```

Enter a password (e.g., yourpassword), then exit (\q). Enable md5 authentication:

```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
```

Add or edit:

```
local   all             postgres                                md5
host    all             postgres         127.0.0.1/32        md5
```

Save and restart:

```bash
sudo service postgresql restart
```

### 4. Create the Database

Create the late_show_db database:

```bash
createdb -U postgres -p 5432 -h localhost late_show_db
```

Enter the postgres password.

### 5. Set Up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 6. Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-migrate psycopg2-binary flask-jwt-extended
```

### 7. Configure Flask

Edit `server/config.py`:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:yourpassword@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your-secret-key"  # Generate with: python -c "import secrets; print(secrets.token_hex(16))"
```

### 8. Initialize and Run Migrations

```bash
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 9. Seed the Database

Populate the database with initial data:

```bash
python server/seed.py
```

### 10. Run the Flask App

```bash
flask run
```

The API will be available at `http://localhost:5000`.

### 11. Test with Postman

Import `challenge-4-lateshow.postman_collection.json` into Postman. Test endpoints:

- **Register**: `POST http://localhost:5000/register`
  ```json
  {"username": "testuser", "password": "testpass"}
  ```

- **Login**: `POST http://localhost:5000/login`
  ```json
  {"username": "testuser", "password": "testpass"}
  ```

Copy the JWT token from the response. Get Episodes: `GET http://localhost:5000/episodes` Create Appearance: `POST http://localhost:5000/appearances` Header: `Authorization: Bearer <token>` Body:
```json
{"rating": 4, "guest_id": 1, "episode_id": 1}
```

Troubleshooting
---------------

- **ImportError in app.py**: Ensure `server/__init__.py` exists:
  ```bash
  touch server/__init__.py
  ```

  Check `server/config.py` imports in `server/app.py`.

- **No db Command**: Reinstall Flask-Migrate:
  ```bash
  pip install --force-reinstall flask-migrate
  ```

- **Database Connection Issues**: Verify `late_show_db`:
  ```bash
  psql -U postgres -p 5432 -h localhost -c "\l"
  ```

  Check `SQLALCHEMY_DATABASE_URI` credentials.

- **Port Conflicts**: Free port 5000:
  ```bash
  lsof -i :5000
  kill -9 <pid>
  ```

- **Permission Issues**: Fix ownership:
  ```bash
  sudo chown -R $USER:$USER /home/user/late-show-api-challenge
  ```

Resetting the Database
-----------------------

To start fresh (e.g., after deleting migrations/):

```bash
dropdb -U postgres -p 5432 -h localhost late_show_db
createdb -U postgres -p 5432 -h localhost late_show_db
rm -rf migrations/
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
```

Contributing
------------

Feel free to submit issues or pull requests to improve the project.

License
-------

This project is licensed under the MIT License.