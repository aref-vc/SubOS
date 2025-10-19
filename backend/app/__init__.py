"""
SubOS Backend Application Factory
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()


def create_app(config_name='default'):
    """
    Application factory pattern

    Args:
        config_name: Configuration to use (development, testing, production)

    Returns:
        Flask application instance
    """
    from app.config import config

    # Create Flask app
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)

    # Configure CORS
    CORS(app,
         supports_credentials=True,
         origins=app.config['CORS_ORIGINS'])

    # Register blueprints
    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'service': 'SubOS API'}, 200

    @app.route('/')
    def index():
        return {
            'name': 'SubOS API',
            'version': '1.0.0',
            'description': 'Self-hosted subscription manager with AI insights',
            'endpoints': {
                'health': '/health',
                'api': '/api/v1',
                'docs': '/api/docs'
            }
        }, 200

    return app
