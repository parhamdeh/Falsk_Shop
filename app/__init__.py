from flask import Flask
import config
from utils import db
from app.routes.product_routes import product_bp
from app.routes.main_routes import main_bp
from app.routes.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.SECRET_KEY
    
    # Initialize database
    db.MongoManager()
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(auth_bp, url_prefix='/login')
    
    return app