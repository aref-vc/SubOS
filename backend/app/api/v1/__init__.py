"""
API v1 Blueprint
"""
from flask import Blueprint

# Create API v1 blueprint
api_v1 = Blueprint('api_v1', __name__)

# Import and register sub-blueprints
from app.api.v1.auth import auth_bp
from app.api.v1.subscriptions import subscriptions_bp
from app.api.v1.budget import budget_bp

api_v1.register_blueprint(auth_bp, url_prefix='/auth')
api_v1.register_blueprint(subscriptions_bp, url_prefix='/subscriptions')
api_v1.register_blueprint(budget_bp, url_prefix='/budget')


@api_v1.route('/status')
def status():
    """API status endpoint"""
    return {
        'status': 'active',
        'version': 'v1',
        'message': 'SubOS API v1 is running',
        'endpoints': {
            'auth': '/api/v1/auth/*',
            'subscriptions': '/api/v1/subscriptions',
            'budget': '/api/v1/budget',
            'currencies': '/api/v1/currencies (coming soon)',
            'categories': '/api/v1/categories (coming soon)',
            'payment_methods': '/api/v1/payment-methods (coming soon)'
        }
    }, 200
