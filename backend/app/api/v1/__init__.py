"""
API v1 Blueprint
"""
from flask import Blueprint

# Create API v1 blueprint
api_v1 = Blueprint('api_v1', __name__)

# Import and register sub-blueprints
from app.api.v1.auth import auth_bp

api_v1.register_blueprint(auth_bp, url_prefix='/auth')


@api_v1.route('/status')
def status():
    """API status endpoint"""
    return {
        'status': 'active',
        'version': 'v1',
        'message': 'SubOS API v1 is running',
        'endpoints': {
            'auth': '/api/v1/auth/*',
            'subscriptions': '/api/v1/subscriptions (coming soon)',
            'currencies': '/api/v1/currencies (coming soon)',
            'budget': '/api/v1/budget (coming soon)'
        }
    }, 200
