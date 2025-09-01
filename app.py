import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from database import init_db, db
from routes.auth import auth_bp
from routes.user import user_bp

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///users.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key-change-me")

    init_db(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(user_bp, url_prefix="/api/v1/users")

    @app.route("/")
    def index():
        return jsonify({"status": "ok", "message": "Flask User API running"})

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
