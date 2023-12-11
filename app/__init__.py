# app/__init__.py

from flask import Flask
from .views import app_views
from .models import db
from .utils.ai_helpers import init_ai
from .utils.db_helpers import init_db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Initialize database
    db.init_app(app)

    # Initialize AI models
    init_ai()

    # Register blueprints
    app.register_blueprint(app_views)

    return app
