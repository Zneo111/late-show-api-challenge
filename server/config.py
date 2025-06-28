from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Tevin20@localhost:5432/late_show_db"
JWT_SECRET_KEY = "<your_jwt_secret>"
