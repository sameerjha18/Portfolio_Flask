from flask import Flask
from .blueprints.main import main_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_bp)
    
    # More blueprints can be registered here

    return app