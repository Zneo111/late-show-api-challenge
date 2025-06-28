from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import models so Flask-Migrate can detect them
    from models.user import User
    from models.guest import Guest
    from models.episode import Episode
    from models.appearance import Appearance

    # Import and register blueprints
    from controllers.guest_controller import guest_bp
    from controllers.episode_controller import episode_bp
    from controllers.appearance_controller import appearance_bp
    from controllers.auth_controller import auth_bp

    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(auth_bp)

    return app

# Allow running with `python server/app.py`
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
