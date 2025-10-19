"""
API v1 Blueprint
"""
from flask import Blueprint

# Create API v1 blueprint
api_v1 = Blueprint('api_v1', __name__)

# Import routes to register them
# We'll add these in future commits
# from app.api.v1 import auth, subscriptions, currencies, budget

@api_v1.route('/status')
def status():
    """API status endpoint"""
    return {
        'status': 'active',
        'version': 'v1',
        'message': 'SubOS API v1 is running'
    }, 200
