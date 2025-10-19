# SubOS - Personal Subscription Manager
## Implementation Plan

**Version**: 1.0
**Date**: October 19, 2025
**Tech Stack**: Python (Flask/FastAPI) + SQLite + React + TypeScript
**Port**: 3038
**Design System**: Integrations UI (Clean & Minimal)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Development Roadmap](#development-roadmap)
3. [Phase 1: Foundation](#phase-1-foundation)
4. [Phase 2: Core Features](#phase-2-core-features)
5. [Phase 3: Notifications](#phase-3-notifications)
6. [Phase 4: Advanced Features](#phase-4-advanced-features)
7. [Phase 5: Enhanced Features](#phase-5-enhanced-features)
8. [Phase 6: Frontend](#phase-6-frontend)
9. [Phase 7: Testing & Deployment](#phase-7-testing--deployment)
10. [Technical Stack Details](#technical-stack-details)
11. [Deployment Options](#deployment-options)
12. [Testing Strategy](#testing-strategy)

---

## 1. Project Overview

### 1.1 Project Structure

```
SubOS/
├── backend/                      # Flask/FastAPI application
│   ├── app/
│   │   ├── __init__.py          # App factory
│   │   ├── models/              # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── subscription.py
│   │   │   ├── currency.py
│   │   │   ├── category.py
│   │   │   ├── household.py
│   │   │   ├── payment_method.py
│   │   │   ├── notification.py
│   │   │   ├── receipt.py
│   │   │   └── insight.py
│   │   ├── api/                 # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── subscriptions.py
│   │   │   │   ├── currencies.py
│   │   │   │   ├── budget.py
│   │   │   │   ├── notifications.py
│   │   │   │   ├── ocr.py
│   │   │   │   ├── insights.py
│   │   │   │   ├── stats.py
│   │   │   │   ├── categories.py
│   │   │   │   ├── payment_methods.py
│   │   │   │   └── household.py
│   │   ├── services/            # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── billing_cycle.py
│   │   │   ├── currency_converter.py
│   │   │   ├── budget_analyzer.py
│   │   │   ├── notification_service.py
│   │   │   ├── ocr_service.py
│   │   │   ├── ml_insights.py
│   │   │   ├── ai_recommendations.py
│   │   │   └── logo_service.py
│   │   ├── tasks/               # Scheduled jobs
│   │   │   ├── __init__.py
│   │   │   ├── currency_updater.py
│   │   │   ├── payment_notifier.py
│   │   │   └── insight_generator.py
│   │   ├── utils/               # Utilities
│   │   │   ├── __init__.py
│   │   │   ├── validators.py
│   │   │   ├── encryption.py
│   │   │   ├── image_processor.py
│   │   │   └── date_calculator.py
│   │   ├── migrations/          # Database migrations
│   │   │   └── versions/
│   │   └── config.py            # Configuration
│   ├── tests/                   # Backend tests
│   │   ├── unit/
│   │   ├── integration/
│   │   └── conftest.py
│   ├── requirements.txt         # Python dependencies
│   ├── alembic.ini             # Migration config
│   └── run.py                   # Application entry point
├── frontend/                    # React application
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/          # React components
│   │   │   ├── common/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   ├── Card.tsx
│   │   │   │   ├── Button.tsx
│   │   │   │   └── Modal.tsx
│   │   │   ├── subscriptions/
│   │   │   │   ├── SubscriptionList.tsx
│   │   │   │   ├── SubscriptionCard.tsx
│   │   │   │   ├── SubscriptionForm.tsx
│   │   │   │   └── SubscriptionModal.tsx
│   │   │   ├── dashboard/
│   │   │   │   ├── Dashboard.tsx
│   │   │   │   ├── SummaryCards.tsx
│   │   │   │   ├── UpcomingPayments.tsx
│   │   │   │   └── RecommendationCards.tsx
│   │   │   ├── insights/
│   │   │   │   ├── InsightsDashboard.tsx
│   │   │   │   ├── SpendingHeatmap.tsx
│   │   │   │   ├── ForecastChart.tsx
│   │   │   │   └── AnomalyTimeline.tsx
│   │   │   ├── ocr/
│   │   │   │   ├── ReceiptUpload.tsx
│   │   │   │   ├── OCRReview.tsx
│   │   │   │   └── ReceiptGallery.tsx
│   │   │   └── settings/
│   │   │       ├── SettingsLayout.tsx
│   │   │       ├── ProfileSettings.tsx
│   │   │       ├── BudgetSettings.tsx
│   │   │       ├── NotificationSettings.tsx
│   │   │       └── SecuritySettings.tsx
│   │   ├── pages/               # Page components
│   │   │   ├── DashboardPage.tsx
│   │   │   ├── SubscriptionsPage.tsx
│   │   │   ├── CalendarPage.tsx
│   │   │   ├── StatisticsPage.tsx
│   │   │   ├── InsightsPage.tsx
│   │   │   ├── OCRPage.tsx
│   │   │   ├── SettingsPage.tsx
│   │   │   └── LoginPage.tsx
│   │   ├── services/            # API client
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   └── subscriptions.ts
│   │   ├── hooks/               # Custom hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useSubscriptions.ts
│   │   │   └── useStats.ts
│   │   ├── styles/              # CSS files
│   │   │   ├── index.css
│   │   │   └── integrations.css
│   │   ├── types/               # TypeScript types
│   │   │   └── index.ts
│   │   ├── utils/               # Frontend utilities
│   │   │   └── formatters.ts
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── docker/                      # Docker configuration (optional)
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── nginx.conf
├── docker-compose.yml           # Docker orchestration (optional)
├── scripts/                     # Utility scripts
│   ├── start.sh                 # Local startup script
│   ├── init_db.py              # Database initialization
│   └── seed_data.py            # Sample data seeding
├── .env.example                 # Environment variables template
├── .gitignore
├── README.md
├── PRD.md                       # Product Requirements Document
└── IMPLEMENTATION_PLAN.md       # This document
```

### 1.2 Development Environment Setup

#### Prerequisites
- Python 3.11+
- Node.js 18+
- SQLite 3
- Git
- (Optional) Docker & Docker Compose

#### Initial Setup
```bash
# Clone repository
git clone <repository-url>
cd SubOS

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Environment configuration
cp .env.example .env
# Edit .env with your configurations
```

---

## 2. Development Roadmap

### Timeline Overview (18 Weeks)

| Phase | Duration | Focus Area | Deliverables |
|-------|----------|------------|--------------|
| 1 | Week 1-2 | Foundation | Database schema, models, basic API structure |
| 2 | Week 3-5 | Core Features | Subscription CRUD, auth, currencies, budget |
| 3 | Week 6-7 | Notifications | 9 notification channels, scheduling |
| 4 | Week 8-10 | Advanced Features | Household, AI, logos, analytics, calendar |
| 5 | Week 11-13 | Enhanced Features | ML insights, OCR, predictive analytics |
| 6 | Week 14-16 | Frontend | React UI, all pages, responsive design |
| 7 | Week 17-18 | Testing & Deploy | Tests, Docker, docs, launch |

---

## 3. Phase 1: Foundation (Week 1-2)

### Objectives
- Set up project structure
- Implement database schema
- Create SQLAlchemy models
- Build migration system
- Establish basic Flask/FastAPI app

### 3.1 Database Setup

#### Step 1.1: Install Dependencies
```bash
cd backend
pip install flask sqlalchemy alembic python-dotenv bcrypt pyotp
# OR for FastAPI
pip install fastapi uvicorn sqlalchemy alembic python-dotenv bcrypt pyotp
```

#### Step 1.2: Database Configuration

**File**: `backend/app/config.py`
```python
import os
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent.parent
    DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR}/subos.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application
    PORT = 3038
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # Session
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    SESSION_COOKIE_SECURE = not DEBUG
    PERMANENT_SESSION_LIFETIME = 2592000  # 30 days

    # File upload
    UPLOAD_FOLDER = BASE_DIR / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'svg'}
```

#### Step 1.3: SQLAlchemy Models

**File**: `backend/app/models/user.py`
```python
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  # bcrypt hash
    email = Column(String(255), unique=True, nullable=False, index=True)
    firstname = Column(String(100))
    main_currency = Column(Integer)  # FK to currencies
    budget = Column(Float)
    avatar = Column(String(255))
    is_admin = Column(Boolean, default=False)
    totp_secret = Column(String(255))
    totp_enabled = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    subscriptions = relationship('Subscription', back_populates='user', cascade='all, delete-orphan')
    currencies = relationship('Currency', back_populates='user', cascade='all, delete-orphan')
    categories = relationship('Category', back_populates='user', cascade='all, delete-orphan')
    household_members = relationship('HouseholdMember', back_populates='user', cascade='all, delete-orphan')
    payment_methods = relationship('PaymentMethod', back_populates='user', cascade='all, delete-orphan')
```

**File**: `backend/app/models/subscription.py`
```python
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    currency_id = Column(Integer, ForeignKey('currencies.id'), nullable=False)
    cycle = Column(Integer, nullable=False)  # 1=days, 2=weeks, 3=months, 4=years
    frequency = Column(Integer, nullable=False, default=1)
    next_payment = Column(Date)
    auto_renew = Column(Boolean, default=True)
    logo = Column(String(255))
    url = Column(String(500))
    notes = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'))
    payer_user_id = Column(Integer, ForeignKey('household.id', ondelete='SET NULL'))
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id', ondelete='SET NULL'))
    inactive = Column(Boolean, default=False, index=True)
    cancellation_date = Column(Date)
    replacement_subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    notify_days_before = Column(Integer, default=7)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship('User', back_populates='subscriptions')
    currency = relationship('Currency')
    category = relationship('Category')
    payer = relationship('HouseholdMember')
    payment_method = relationship('PaymentMethod')
    receipts = relationship('Receipt', back_populates='subscription', cascade='all, delete-orphan')
```

**File**: `backend/app/models/__init__.py`
```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models.user import User
from app.models.subscription import Subscription
from app.models.currency import Currency
from app.models.category import Category
from app.models.household import HouseholdMember
from app.models.payment_method import PaymentMethod
from app.models.notification import (
    NotificationSettings, EmailNotification, DiscordNotification,
    TelegramNotification, PushoverNotification, WebhookNotification
)
from app.models.receipt import Receipt
from app.models.insight import AIRecommendation, MLInsight, NotificationLog
```

*(Continue creating other models following the schema in PRD.md)*

#### Step 1.4: Database Migration

**File**: `backend/alembic.ini`
```ini
[alembic]
script_location = app/migrations
sqlalchemy.url = sqlite:///subos.db

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

**Initialize Alembic**:
```bash
cd backend
alembic init app/migrations
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head
```

#### Step 1.5: Basic Flask Application

**File**: `backend/app/__init__.py`
```python
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    CORS(app, supports_credentials=True, origins=['http://localhost:5173'])

    # Register blueprints
    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app
```

**File**: `backend/run.py`
```python
from app import create_app
from app.config import Config

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)
```

### Deliverables (Phase 1)
- ✅ Project structure created
- ✅ Database schema implemented (all tables)
- ✅ SQLAlchemy models created (15+ models)
- ✅ Migration system configured
- ✅ Basic Flask app running on port 3038
- ✅ Environment configuration setup

---

## 4. Phase 2: Core Features (Week 3-5)

### Objectives
- Authentication system (local + OAuth)
- Subscription CRUD endpoints
- Multi-currency support
- Budget tracking
- Billing cycle calculator

### 4.1 Authentication System

#### Step 2.1: Install Auth Dependencies
```bash
pip install flask-login pyjwt flask-bcrypt pyotp qrcode
```

#### Step 2.2: Authentication Service

**File**: `backend/app/services/auth_service.py`
```python
import bcrypt
import pyotp
import jwt
from datetime import datetime, timedelta
from app.models.user import User
from app import db
from app.config import Config

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt"""
        salt = bcrypt.gensalt(rounds=12)
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

    @staticmethod
    def generate_totp_secret() -> str:
        """Generate TOTP secret for 2FA"""
        return pyotp.random_base32()

    @staticmethod
    def verify_totp(secret: str, code: str) -> bool:
        """Verify TOTP code"""
        totp = pyotp.TOTP(secret)
        return totp.verify(code, valid_window=1)

    @staticmethod
    def generate_token(user_id: int) -> str:
        """Generate JWT token"""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=30)
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def verify_token(token: str) -> int:
        """Verify JWT token and return user_id"""
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
```

#### Step 2.3: Auth Endpoints

**File**: `backend/app/api/v1/auth.py`
```python
from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app.models.user import User
from app import db
from app.utils.validators import validate_email, validate_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register new user"""
    data = request.get_json()

    # Validation
    if not validate_email(data.get('email')):
        return jsonify({'status': 'error', 'message': 'Invalid email'}), 400

    if not validate_password(data.get('password')):
        return jsonify({'status': 'error', 'message': 'Password must be at least 8 characters'}), 400

    # Check if user exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'status': 'error', 'message': 'Username already exists'}), 409

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'status': 'error', 'message': 'Email already registered'}), 409

    # Create user
    user = User(
        username=data['username'],
        email=data['email'],
        password=AuthService.hash_password(data['password']),
        firstname=data.get('firstname')
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'User registered successfully',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if not user or not AuthService.verify_password(data['password'], user.password):
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

    # Check if 2FA is enabled
    if user.totp_enabled:
        if 'totp_code' not in data:
            return jsonify({'status': 'error', 'message': '2FA code required'}), 401

        if not AuthService.verify_totp(user.totp_secret, data['totp_code']):
            return jsonify({'status': 'error', 'message': 'Invalid 2FA code'}), 401

    # Generate token
    token = AuthService.generate_token(user.id)

    return jsonify({
        'status': 'success',
        'token': token,
        'user': {
            'id': user.id,
            'username': user.username,
            'is_admin': user.is_admin
        }
    }), 200
```

### 4.2 Subscription CRUD

#### Step 2.4: Billing Cycle Calculator

**File**: `backend/app/services/billing_cycle.py`
```python
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class BillingCycleCalculator:
    CYCLE_DAYS = 1
    CYCLE_WEEKS = 2
    CYCLE_MONTHS = 3
    CYCLE_YEARS = 4

    @staticmethod
    def calculate_next_payment(start_date: datetime, cycle: int, frequency: int) -> datetime:
        """Calculate next payment date based on cycle and frequency"""
        if cycle == BillingCycleCalculator.CYCLE_DAYS:
            return start_date + timedelta(days=frequency)

        elif cycle == BillingCycleCalculator.CYCLE_WEEKS:
            return start_date + timedelta(weeks=frequency)

        elif cycle == BillingCycleCalculator.CYCLE_MONTHS:
            return start_date + relativedelta(months=frequency)

        elif cycle == BillingCycleCalculator.CYCLE_YEARS:
            return start_date + relativedelta(years=frequency)

        else:
            raise ValueError(f"Invalid cycle: {cycle}")

    @staticmethod
    def calculate_monthly_cost(price: float, cycle: int, frequency: int) -> float:
        """Convert subscription price to monthly equivalent"""
        if cycle == BillingCycleCalculator.CYCLE_DAYS:
            return (price / frequency) * 30.44  # Average days per month

        elif cycle == BillingCycleCalculator.CYCLE_WEEKS:
            return (price / frequency) * 4.33  # Average weeks per month

        elif cycle == BillingCycleCalculator.CYCLE_MONTHS:
            return price / frequency

        elif cycle == BillingCycleCalculator.CYCLE_YEARS:
            return price / (frequency * 12)

        else:
            raise ValueError(f"Invalid cycle: {cycle}")
```

#### Step 2.5: Subscription Endpoints

**File**: `backend/app/api/v1/subscriptions.py`
```python
from flask import Blueprint, request, jsonify, g
from app.models.subscription import Subscription
from app.services.billing_cycle import BillingCycleCalculator
from app.utils.decorators import require_auth
from app import db

subscriptions_bp = Blueprint('subscriptions', __name__)

@subscriptions_bp.route('', methods=['GET'])
@require_auth
def list_subscriptions():
    """List all subscriptions for current user"""
    user_id = g.user_id

    # Query parameters
    inactive = request.args.get('inactive', 'false').lower() == 'true'
    category_id = request.args.get('category_id', type=int)
    sort = request.args.get('sort', 'name')
    order = request.args.get('order', 'asc')

    # Build query
    query = Subscription.query.filter_by(user_id=user_id)

    if not inactive:
        query = query.filter_by(inactive=False)

    if category_id:
        query = query.filter_by(category_id=category_id)

    # Sort
    if order == 'desc':
        query = query.order_by(getattr(Subscription, sort).desc())
    else:
        query = query.order_by(getattr(Subscription, sort).asc())

    subscriptions = query.all()

    return jsonify({
        'status': 'success',
        'data': [sub.to_dict() for sub in subscriptions],
        'total': len(subscriptions)
    }), 200

@subscriptions_bp.route('', methods=['POST'])
@require_auth
def create_subscription():
    """Create new subscription"""
    user_id = g.user_id
    data = request.get_json()

    # Calculate next payment date if not provided
    if 'next_payment' not in data:
        start_date = datetime.now()
        data['next_payment'] = BillingCycleCalculator.calculate_next_payment(
            start_date, data['cycle'], data['frequency']
        )

    subscription = Subscription(
        user_id=user_id,
        **data
    )

    db.session.add(subscription)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'data': subscription.to_dict()
    }), 201

@subscriptions_bp.route('/<int:subscription_id>', methods=['GET'])
@require_auth
def get_subscription(subscription_id):
    """Get subscription details"""
    subscription = Subscription.query.filter_by(
        id=subscription_id,
        user_id=g.user_id
    ).first_or_404()

    return jsonify({
        'status': 'success',
        'data': subscription.to_dict()
    }), 200

@subscriptions_bp.route('/<int:subscription_id>', methods=['PUT'])
@require_auth
def update_subscription(subscription_id):
    """Update subscription"""
    subscription = Subscription.query.filter_by(
        id=subscription_id,
        user_id=g.user_id
    ).first_or_404()

    data = request.get_json()

    # Update fields
    for key, value in data.items():
        if hasattr(subscription, key):
            setattr(subscription, key, value)

    db.session.commit()

    return jsonify({
        'status': 'success',
        'data': subscription.to_dict()
    }), 200

@subscriptions_bp.route('/<int:subscription_id>', methods=['DELETE'])
@require_auth
def delete_subscription(subscription_id):
    """Delete subscription"""
    subscription = Subscription.query.filter_by(
        id=subscription_id,
        user_id=g.user_id
    ).first_or_404()

    db.session.delete(subscription)
    db.session.commit()

    return '', 204
```

### 4.3 Currency Management

#### Step 2.6: Currency Converter Service

**File**: `backend/app/services/currency_converter.py`
```python
import requests
from datetime import datetime
from app.models.currency import Currency
from app.config import Config
from app import db

class CurrencyConverter:
    FIXER_API_URL = 'https://api.fixer.io/latest'

    @staticmethod
    def update_exchange_rates(api_key: str):
        """Fetch and update exchange rates from Fixer.io"""
        try:
            response = requests.get(
                CurrencyConverter.FIXER_API_URL,
                params={'access_key': api_key}
            )
            data = response.json()

            if not data.get('success'):
                raise Exception('Failed to fetch exchange rates')

            # Update rates in database
            for code, rate in data['rates'].items():
                currencies = Currency.query.filter_by(code=code).all()
                for currency in currencies:
                    currency.rate = rate
                    currency.last_updated = datetime.now()

            db.session.commit()
            return True

        except Exception as e:
            print(f"Error updating exchange rates: {e}")
            return False

    @staticmethod
    def convert(amount: float, from_currency_id: int, to_currency_id: int) -> float:
        """Convert amount from one currency to another"""
        from_currency = Currency.query.get(from_currency_id)
        to_currency = Currency.query.get(to_currency_id)

        if not from_currency or not to_currency:
            raise ValueError('Invalid currency ID')

        # Convert to USD first, then to target currency
        amount_in_usd = amount / from_currency.rate
        return amount_in_usd * to_currency.rate
```

### 4.4 Budget Tracking

#### Step 2.7: Budget Analyzer

**File**: `backend/app/services/budget_analyzer.py`
```python
from sqlalchemy import func
from app.models.subscription import Subscription
from app.models.user import User
from app.services.billing_cycle import BillingCycleCalculator
from app.services.currency_converter import CurrencyConverter

class BudgetAnalyzer:
    @staticmethod
    def calculate_monthly_spending(user_id: int) -> float:
        """Calculate total monthly spending for user"""
        user = User.query.get(user_id)
        subscriptions = Subscription.query.filter_by(
            user_id=user_id,
            inactive=False
        ).all()

        total = 0.0
        for sub in subscriptions:
            # Calculate monthly cost
            monthly_cost = BillingCycleCalculator.calculate_monthly_cost(
                sub.price, sub.cycle, sub.frequency
            )

            # Convert to user's main currency
            if user.main_currency and sub.currency_id != user.main_currency:
                monthly_cost = CurrencyConverter.convert(
                    monthly_cost,
                    sub.currency_id,
                    user.main_currency
                )

            total += monthly_cost

        return total

    @staticmethod
    def get_budget_status(user_id: int) -> dict:
        """Get budget status for user"""
        user = User.query.get(user_id)
        monthly_spending = BudgetAnalyzer.calculate_monthly_spending(user_id)

        budget = user.budget or 0
        utilization = (monthly_spending / budget * 100) if budget > 0 else 0

        return {
            'monthly_budget': budget,
            'current_spending': round(monthly_spending, 2),
            'utilization': round(utilization, 2),
            'projected_yearly': round(monthly_spending * 12, 2),
            'remaining': round(budget - monthly_spending, 2)
        }

    @staticmethod
    def calculate_savings_from_inactive(user_id: int) -> float:
        """Calculate savings from inactive subscriptions"""
        inactive_subs = Subscription.query.filter_by(
            user_id=user_id,
            inactive=True
        ).all()

        total_savings = 0.0
        for sub in inactive_subs:
            monthly_cost = BillingCycleCalculator.calculate_monthly_cost(
                sub.price, sub.cycle, sub.frequency
            )
            total_savings += monthly_cost

        return round(total_savings, 2)
```

### Deliverables (Phase 2)
- ✅ Authentication system (register, login, JWT)
- ✅ TOTP 2FA implementation
- ✅ Subscription CRUD endpoints (5 endpoints)
- ✅ Billing cycle calculator
- ✅ Currency converter service
- ✅ Budget analyzer service
- ✅ Currency endpoints
- ✅ Budget endpoints

---

## 5. Phase 3: Notifications (Week 6-7)

### Objectives
- Implement 9 notification channels
- Build notification scheduler
- Create notification templates
- Set up cron jobs

### 5.1 Notification Service

#### Step 3.1: Install Dependencies
```bash
pip install apscheduler requests python-telegram-bot discord-webhook
```

#### Step 3.2: Base Notification Service

**File**: `backend/app/services/notification_service.py`
```python
from abc import ABC, abstractmethod
from typing import Dict, Any
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from app.models.notification import (
    EmailNotification, DiscordNotification, TelegramNotification,
    PushoverNotification, WebhookNotification
)

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        """Send notification"""
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, config: EmailNotification):
        self.config = config

    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config.from_email
            msg['To'] = recipient

            html_part = MIMEText(message, 'html')
            msg.attach(html_part)

            with smtplib.SMTP(self.config.smtp_host, self.config.smtp_port) as server:
                if self.config.use_tls:
                    server.starttls()
                server.login(self.config.smtp_username, self.config.smtp_password)
                server.send_message(msg)

            return True
        except Exception as e:
            print(f"Email send error: {e}")
            return False

class DiscordChannel(NotificationChannel):
    def __init__(self, config: DiscordNotification):
        self.webhook_url = config.webhook_url

    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        try:
            payload = {
                'embeds': [{
                    'title': subject,
                    'description': message,
                    'color': 0xF2580A  # Integrations UI accent color
                }]
            }
            response = requests.post(self.webhook_url, json=payload)
            return response.status_code == 204
        except Exception as e:
            print(f"Discord send error: {e}")
            return False

class TelegramChannel(NotificationChannel):
    def __init__(self, config: TelegramNotification):
        self.bot_token = config.bot_token
        self.chat_id = config.chat_id

    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        try:
            url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
            payload = {
                'chat_id': self.chat_id,
                'text': f'*{subject}*\n\n{message}',
                'parse_mode': 'Markdown'
            }
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram send error: {e}")
            return False

class PushoverChannel(NotificationChannel):
    def __init__(self, config: PushoverNotification):
        self.user_key = config.user_key
        self.api_token = config.api_token

    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        try:
            payload = {
                'token': self.api_token,
                'user': self.user_key,
                'title': subject,
                'message': message
            }
            response = requests.post('https://api.pushover.net/1/messages.json', data=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Pushover send error: {e}")
            return False

class WebhookChannel(NotificationChannel):
    def __init__(self, config: WebhookNotification):
        self.webhook_url = config.webhook_url
        self.payload_template = config.payload_template
        self.method = config.method

    def send(self, recipient: str, subject: str, message: str, **kwargs) -> bool:
        try:
            # Replace template variables
            payload = self.payload_template.replace('{{subject}}', subject)
            payload = payload.replace('{{message}}', message)

            if self.method == 'POST':
                response = requests.post(self.webhook_url, data=payload)
            else:
                response = requests.get(self.webhook_url, params={'message': message})

            return response.status_code < 400
        except Exception as e:
            print(f"Webhook send error: {e}")
            return False

class NotificationService:
    @staticmethod
    def send_notification(user_id: int, channel: str, subject: str, message: str) -> bool:
        """Send notification through specified channel"""
        # Get channel configuration
        if channel == 'email':
            config = EmailNotification.query.filter_by(user_id=user_id).first()
            if config:
                return EmailChannel(config).send(config.from_email, subject, message)

        elif channel == 'discord':
            config = DiscordNotification.query.filter_by(user_id=user_id).first()
            if config:
                return DiscordChannel(config).send('', subject, message)

        elif channel == 'telegram':
            config = TelegramNotification.query.filter_by(user_id=user_id).first()
            if config:
                return TelegramChannel(config).send('', subject, message)

        # Add other channels...

        return False
```

### 5.2 Notification Scheduler

#### Step 3.3: Payment Reminder Task

**File**: `backend/app/tasks/payment_notifier.py`
```python
from datetime import datetime, timedelta
from app.models.subscription import Subscription
from app.models.user import User
from app.models.notification import NotificationSettings, NotificationLog
from app.services.notification_service import NotificationService
from app import db

class PaymentNotifier:
    @staticmethod
    def send_upcoming_payment_notifications():
        """Send notifications for upcoming payments"""
        # Get all active subscriptions
        subscriptions = Subscription.query.filter_by(inactive=False).all()

        for sub in subscriptions:
            # Get user notification settings
            settings = NotificationSettings.query.filter_by(user_id=sub.user_id).first()
            if not settings:
                continue

            days_before = sub.notify_days_before or settings.days_before
            notify_date = sub.next_payment - timedelta(days=days_before)

            # Check if we should send notification today
            if notify_date.date() == datetime.now().date():
                # Build notification message
                subject = f"Upcoming Payment: {sub.name}"
                message = f"""
                Your {sub.name} subscription payment of {sub.currency.symbol}{sub.price}
                is due on {sub.next_payment.strftime('%Y-%m-%d')}.
                """

                # Send through enabled channels
                if settings.email_enabled:
                    success = NotificationService.send_notification(
                        sub.user_id, 'email', subject, message
                    )
                    PaymentNotifier._log_notification(
                        sub.user_id, sub.id, 'email', 'upcoming', success
                    )

                if settings.discord_enabled:
                    success = NotificationService.send_notification(
                        sub.user_id, 'discord', subject, message
                    )
                    PaymentNotifier._log_notification(
                        sub.user_id, sub.id, 'discord', 'upcoming', success
                    )

                # Add other channels...

    @staticmethod
    def _log_notification(user_id: int, subscription_id: int, channel: str,
                         notification_type: str, success: bool):
        """Log notification send attempt"""
        log = NotificationLog(
            user_id=user_id,
            subscription_id=subscription_id,
            channel=channel,
            notification_type=notification_type,
            status='sent' if success else 'failed'
        )
        db.session.add(log)
        db.session.commit()
```

#### Step 3.4: Scheduler Setup

**File**: `backend/app/tasks/__init__.py`
```python
from apscheduler.schedulers.background import BackgroundScheduler
from app.tasks.payment_notifier import PaymentNotifier
from app.tasks.currency_updater import CurrencyUpdater

def init_scheduler():
    """Initialize APScheduler for background tasks"""
    scheduler = BackgroundScheduler()

    # Daily at 9:00 AM - Send payment notifications
    scheduler.add_job(
        PaymentNotifier.send_upcoming_payment_notifications,
        'cron',
        hour=9,
        minute=0,
        id='payment_notifications'
    )

    # Daily at 2:00 AM - Update currency rates
    scheduler.add_job(
        CurrencyUpdater.update_all_rates,
        'cron',
        hour=2,
        minute=0,
        id='currency_update'
    )

    scheduler.start()
    return scheduler
```

### Deliverables (Phase 3)
- ✅ Email notification channel
- ✅ Discord notification channel
- ✅ Telegram notification channel
- ✅ Pushover notification channel
- ✅ Webhook notification channel
- ✅ (Implement 4 more channels similarly)
- ✅ Notification scheduler with cron jobs
- ✅ Notification logging system

---

## 6. Phase 4: Advanced Features (Week 8-10)

### Objectives
- Household member management
- AI-powered recommendations
- Logo search and upload
- Statistics and analytics
- Calendar view

### 6.1 AI Recommendations

#### Step 4.1: Install AI Dependencies
```bash
pip install openai google-generativeai ollama
```

#### Step 4.2: AI Recommendation Service

**File**: `backend/app/services/ai_recommendations.py`
```python
import openai
import google.generativeai as genai
from typing import List, Dict
from app.models.subscription import Subscription
from app.models.ai_recommendation import AIRecommendation
from app import db

class AIRecommendationService:
    @staticmethod
    def analyze_subscriptions_openai(user_id: int, api_key: str) -> List[Dict]:
        """Analyze subscriptions using OpenAI GPT"""
        openai.api_key = api_key

        # Get user subscriptions
        subscriptions = Subscription.query.filter_by(
            user_id=user_id,
            inactive=False
        ).all()

        # Build subscription data
        sub_data = [
            {
                'name': sub.name,
                'price': sub.price,
                'currency': sub.currency.code,
                'category': sub.category.name if sub.category else 'Other'
            }
            for sub in subscriptions
        ]

        # Create prompt
        prompt = f"""
        Analyze the following subscriptions and provide cost-saving recommendations:

        {sub_data}

        Provide recommendations in this JSON format:
        {{
            "recommendations": [
                {{
                    "title": "...",
                    "description": "...",
                    "savings": "...",
                    "type": "duplicate|alternative|bundle|cancel|optimize",
                    "related_subscriptions": [...]
                }}
            ]
        }}

        Focus on:
        1. Duplicate or overlapping services
        2. Cheaper alternatives
        3. Bundle opportunities
        4. Unused or underutilized subscriptions
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial advisor specializing in subscription optimization."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Parse response
        recommendations = response.choices[0].message['content']

        # Store recommendations
        # ... parse JSON and save to database ...

        return recommendations

    @staticmethod
    def analyze_subscriptions_gemini(user_id: int, api_key: str) -> List[Dict]:
        """Analyze subscriptions using Google Gemini"""
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        # Similar implementation to OpenAI
        # ...

    @staticmethod
    def analyze_subscriptions_ollama(user_id: int, model_name: str = 'llama2') -> List[Dict]:
        """Analyze subscriptions using local Ollama"""
        import ollama

        # Similar implementation using Ollama client
        # ...
```

### 6.2 Logo Management

#### Step 4.3: Logo Service

**File**: `backend/app/services/logo_service.py`
```python
import requests
from PIL import Image
from io import BytesIO
import os
from app.config import Config

class LogoService:
    @staticmethod
    def search_logo(query: str) -> List[str]:
        """Search for logo using Clearbit or similar service"""
        # Clearbit Logo API
        url = f"https://logo.clearbit.com/{query}"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return [url]
        except:
            pass

        # Fallback to DuckDuckGo image search or Google Custom Search
        # ...

        return []

    @staticmethod
    def upload_logo(file, subscription_id: int) -> str:
        """Process and save uploaded logo"""
        # Validate file type
        allowed_extensions = Config.ALLOWED_EXTENSIONS
        filename = file.filename.lower()

        if not any(filename.endswith(ext) for ext in allowed_extensions):
            raise ValueError('Invalid file type')

        # Open image
        image = Image.open(file)

        # Resize to 256x256
        image = image.resize((256, 256), Image.Resampling.LANCZOS)

        # Save with subscription ID as filename
        filename = f"sub_{subscription_id}.png"
        filepath = os.path.join(Config.UPLOAD_FOLDER, 'logos', filename)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        image.save(filepath, 'PNG', optimize=True)

        return filename

    @staticmethod
    def download_logo(url: str, subscription_id: int) -> str:
        """Download logo from URL"""
        response = requests.get(url)

        if response.status_code == 200:
            file = BytesIO(response.content)
            return LogoService.upload_logo(file, subscription_id)

        raise Exception('Failed to download logo')
```

### 6.3 Statistics Service

#### Step 4.4: Statistics Calculator

**File**: `backend/app/services/statistics.py`
```python
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.subscription import Subscription
from app.models.category import Category
from app.services.billing_cycle import BillingCycleCalculator

class StatisticsService:
    @staticmethod
    def get_dashboard_overview(user_id: int) -> dict:
        """Get dashboard overview statistics"""
        # Total active subscriptions
        total_active = Subscription.query.filter_by(
            user_id=user_id,
            inactive=False
        ).count()

        # Monthly cost calculation
        # ... (use BudgetAnalyzer)

        # Upcoming payments (next 7 days)
        today = datetime.now().date()
        upcoming = Subscription.query.filter(
            Subscription.user_id == user_id,
            Subscription.inactive == False,
            Subscription.next_payment >= today,
            Subscription.next_payment <= today + timedelta(days=7)
        ).all()

        return {
            'total_active': total_active,
            'monthly_cost': 0,  # Calculate
            'upcoming_count': len(upcoming),
            'upcoming_payments': [sub.to_dict() for sub in upcoming]
        }

    @staticmethod
    def get_spending_trends(user_id: int, period: str = 'month') -> dict:
        """Get spending trends over time"""
        # Implementation for trend calculation
        # ...

    @staticmethod
    def get_category_breakdown(user_id: int) -> dict:
        """Get cost breakdown by category"""
        subscriptions = Subscription.query.filter_by(
            user_id=user_id,
            inactive=False
        ).all()

        category_costs = {}

        for sub in subscriptions:
            category_name = sub.category.name if sub.category else 'Uncategorized'
            monthly_cost = BillingCycleCalculator.calculate_monthly_cost(
                sub.price, sub.cycle, sub.frequency
            )

            if category_name not in category_costs:
                category_costs[category_name] = 0

            category_costs[category_name] += monthly_cost

        return category_costs
```

### Deliverables (Phase 4)
- ✅ Household member CRUD
- ✅ AI recommendations (OpenAI, Gemini, Ollama)
- ✅ Logo search and upload
- ✅ Logo download from URL
- ✅ Statistics service
- ✅ Category breakdown analytics
- ✅ Calendar view data endpoint

---

## 7. Phase 5: Enhanced Features (Week 11-13)

### Objectives
- ML-powered insights dashboard
- Receipt OCR processing
- Anomaly detection
- Predictive analytics

### 7.1 ML Insights

#### Step 5.1: Install ML Dependencies
```bash
pip install scikit-learn pandas numpy statsmodels prophet
```

#### Step 5.2: ML Insights Engine

**File**: `backend/app/services/ml_insights.py`
```python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta
from app.models.subscription import Subscription
from app.models.insight import MLInsight
from app import db

class MLInsightsEngine:
    @staticmethod
    def detect_anomalies(user_id: int) -> List[Dict]:
        """Detect spending anomalies using Isolation Forest"""
        # Get subscription history
        subscriptions = Subscription.query.filter_by(user_id=user_id).all()

        # Build feature matrix
        data = []
        for sub in subscriptions:
            monthly_cost = BillingCycleCalculator.calculate_monthly_cost(
                sub.price, sub.cycle, sub.frequency
            )
            data.append({
                'subscription_id': sub.id,
                'monthly_cost': monthly_cost,
                'created_timestamp': sub.created_at.timestamp()
            })

        if len(data) < 5:
            return []  # Need minimum data points

        df = pd.DataFrame(data)
        X = df[['monthly_cost', 'created_timestamp']].values

        # Fit Isolation Forest
        clf = IsolationForest(contamination=0.1, random_state=42)
        predictions = clf.fit_predict(X)

        # Extract anomalies
        anomalies = []
        for idx, pred in enumerate(predictions):
            if pred == -1:  # Anomaly detected
                sub = subscriptions[idx]
                insight = {
                    'type': 'anomaly',
                    'title': f'Unusual subscription detected: {sub.name}',
                    'description': f'This subscription has unusual cost pattern',
                    'severity': 'warning',
                    'subscription_id': sub.id
                }
                anomalies.append(insight)

        return anomalies

    @staticmethod
    def predict_next_month_cost(user_id: int) -> Dict:
        """Predict next month's cost using ARIMA"""
        # Get historical monthly costs
        # ... (build time series)

        # Fit ARIMA model
        model = ARIMA(historical_costs, order=(1, 1, 1))
        fitted = model.fit()

        # Forecast next month
        forecast = fitted.forecast(steps=1)

        return {
            'predicted_cost': float(forecast[0]),
            'confidence_interval': [float(x) for x in fitted.get_forecast(steps=1).conf_int()[0]]
        }

    @staticmethod
    def cluster_subscriptions(user_id: int) -> Dict:
        """Cluster subscriptions by spending patterns"""
        subscriptions = Subscription.query.filter_by(
            user_id=user_id,
            inactive=False
        ).all()

        if len(subscriptions) < 3:
            return {}

        # Build feature matrix
        features = []
        for sub in subscriptions:
            monthly_cost = BillingCycleCalculator.calculate_monthly_cost(
                sub.price, sub.cycle, sub.frequency
            )
            features.append([monthly_cost])

        X = np.array(features)

        # K-means clustering
        n_clusters = min(3, len(subscriptions))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(X)

        # Group subscriptions by cluster
        clusters = {}
        for idx, label in enumerate(labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append({
                'id': subscriptions[idx].id,
                'name': subscriptions[idx].name,
                'monthly_cost': features[idx][0]
            })

        return clusters
```

### 7.2 OCR Service

#### Step 5.3: Install OCR Dependencies
```bash
pip install pytesseract pillow google-cloud-vision pdf2image
# Also install Tesseract: brew install tesseract (macOS) or apt-get install tesseract-ocr (Linux)
```

#### Step 5.4: OCR Processing Pipeline

**File**: `backend/app/services/ocr_service.py`
```python
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import re
from datetime import datetime
from google.cloud import vision
from app.config import Config

class OCRService:
    @staticmethod
    def preprocess_image(image_path: str) -> Image:
        """Preprocess image for better OCR accuracy"""
        # Open image
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Denoise
        denoised = cv2.fastNlMeansDenoising(gray)

        # Threshold (binarization)
        _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Convert back to PIL Image
        return Image.fromarray(thresh)

    @staticmethod
    def extract_text_tesseract(image_path: str) -> str:
        """Extract text using Tesseract OCR"""
        # Preprocess image
        preprocessed = OCRService.preprocess_image(image_path)

        # Extract text
        text = pytesseract.image_to_string(preprocessed, config='--psm 6')

        return text

    @staticmethod
    def extract_text_google_vision(image_path: str, api_key: str) -> str:
        """Extract text using Google Vision API"""
        client = vision.ImageAnnotatorClient(credentials={'api_key': api_key})

        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)

        if response.error.message:
            raise Exception(response.error.message)

        return response.text_annotations[0].description if response.text_annotations else ''

    @staticmethod
    def parse_subscription_data(text: str) -> Dict:
        """Parse subscription data from extracted text using regex and NLP"""
        data = {
            'name': None,
            'price': None,
            'currency': 'USD',
            'billing_date': None,
            'cycle': None
        }

        # Extract price (pattern: $XX.XX or XX.XX USD)
        price_pattern = r'(?:[$€£]?\s*)?(\d+\.?\d*)\s*(?:USD|EUR|GBP|$|€|£)?'
        price_match = re.search(price_pattern, text, re.IGNORECASE)
        if price_match:
            data['price'] = float(price_match.group(1))

        # Extract date (pattern: MM/DD/YYYY or DD-MM-YYYY)
        date_pattern = r'(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})'
        date_match = re.search(date_pattern, text)
        if date_match:
            try:
                data['billing_date'] = datetime.strptime(date_match.group(1), '%m/%d/%Y').date()
            except:
                try:
                    data['billing_date'] = datetime.strptime(date_match.group(1), '%d-%m-%Y').date()
                except:
                    pass

        # Detect billing cycle
        if re.search(r'monthly|per month|/month', text, re.IGNORECASE):
            data['cycle'] = 3  # Monthly
        elif re.search(r'annual|yearly|per year|/year', text, re.IGNORECASE):
            data['cycle'] = 4  # Yearly

        # Extract service name (first line or brand detection)
        lines = text.split('\n')
        if lines:
            # Common subscription services
            known_services = [
                'Netflix', 'Spotify', 'Apple', 'Amazon', 'Disney', 'HBO',
                'Microsoft', 'Google', 'Adobe', 'Dropbox', 'GitHub'
            ]
            for service in known_services:
                if service.lower() in text.lower():
                    data['name'] = service
                    break

            if not data['name']:
                data['name'] = lines[0].strip()

        return data

    @staticmethod
    def process_receipt(image_path: str, provider: str = 'tesseract', api_key: str = None) -> Dict:
        """Process receipt and extract subscription data"""
        # Extract text
        if provider == 'tesseract':
            text = OCRService.extract_text_tesseract(image_path)
            confidence = 0.75  # Estimated
        elif provider == 'google_vision':
            text = OCRService.extract_text_google_vision(image_path, api_key)
            confidence = 0.95  # Google Vision is more accurate
        else:
            raise ValueError(f'Unknown OCR provider: {provider}')

        # Parse subscription data
        extracted_data = OCRService.parse_subscription_data(text)

        return {
            'raw_text': text,
            'extracted_data': extracted_data,
            'confidence': confidence,
            'provider': provider
        }
```

### Deliverables (Phase 5)
- ✅ Anomaly detection (Isolation Forest)
- ✅ Predictive budgeting (ARIMA)
- ✅ Subscription clustering (K-means)
- ✅ OCR image preprocessing
- ✅ Tesseract OCR integration
- ✅ Google Vision OCR integration
- ✅ Subscription data parsing from receipts
- ✅ ML insights storage and retrieval

---

## 8. Phase 6: Frontend (Week 14-16)

### Objectives
- Build React frontend with TypeScript
- Implement all pages and components
- Integrate with backend API
- Apply Integrations UI design system

### 8.1 Frontend Setup

#### Step 6.1: Initialize React Project
```bash
cd frontend
npm create vite@latest . -- --template react-ts
npm install
```

#### Step 6.2: Install Dependencies
```bash
npm install react-router-dom
npm install @tanstack/react-query
npm install axios
npm install chart.js react-chartjs-2
npm install date-fns
npm install react-hook-form zod @hookform/resolvers
npm install lucide-react
npm install clsx tailwind-merge
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu
```

#### Step 6.3: Tailwind CSS Setup with Integrations UI

**File**: `frontend/tailwind.config.js`
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      colors: {
        // Integrations UI Design System
        'bg-main': '#FAF8F7',
        'bg-white': '#FFFFFF',
        'bg-icon': '#F0F0F0',
        'text-primary': '#1A1A1A',
        'text-secondary': '#6B6B6B',
        'text-light': '#9A9A9A',
        'accent': '#F2580A',
        'toggle-inactive': '#E5E5E5',
        'border-card': '#E8E8E8',
        'divider': '#ECECEC',
      },
    },
  },
  plugins: [],
}
```

**File**: `frontend/src/styles/integrations.css`
```css
:root {
  /* Integrations UI - Clean & minimal design system */
  --font-family: 'JetBrains Mono', monospace;

  /* Backgrounds */
  --bg-main: #FAF8F7;
  --bg-main-rgb: 250, 248, 247;
  --bg-white: #FFFFFF;
  --bg-white-rgb: 255, 255, 255;
  --bg-icon: #F0F0F0;
  --bg-icon-rgb: 240, 240, 240;

  /* Text Colors */
  --text-primary: #1A1A1A;
  --text-primary-rgb: 26, 26, 26;
  --text-secondary: #6B6B6B;
  --text-secondary-rgb: 107, 107, 107;
  --text-light: #9A9A9A;
  --text-light-rgb: 154, 154, 154;

  /* UI Colors */
  --accent: #F2580A;
  --accent-rgb: 242, 88, 10;
  --toggle-inactive: #E5E5E5;
  --toggle-inactive-rgb: 229, 229, 229;

  /* Borders */
  --border-card: #E8E8E8;
  --border-card-rgb: 232, 232, 232;
  --divider: #ECECEC;
  --divider-rgb: 236, 236, 236;
}

body {
  font-family: var(--font-family);
  background: var(--bg-main);
  color: var(--text-primary);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Clean card styling */
.card {
  background: var(--bg-white);
  border: 1px solid var(--border-card);
  border-radius: 12px;
  padding: 24px;
  transition: all 0.2s ease;
}

.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

/* Button styling */
.btn-primary {
  background: var(--accent);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  font-family: var(--font-family);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: #D94D08;
  transform: translateY(-1px);
}

.btn-secondary {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-card);
  padding: 12px 24px;
  border-radius: 8px;
  font-family: var(--font-family);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: var(--bg-icon);
}
```

### 8.2 API Client Setup

**File**: `frontend/src/services/api.ts`
```typescript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:3038/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

**File**: `frontend/src/services/subscriptions.ts`
```typescript
import api from './api';
import { Subscription, SubscriptionCreate } from '../types';

export const subscriptionsApi = {
  list: async (filters?: any) => {
    const { data } = await api.get('/subscriptions', { params: filters });
    return data;
  },

  get: async (id: number) => {
    const { data } = await api.get(`/subscriptions/${id}`);
    return data;
  },

  create: async (subscription: SubscriptionCreate) => {
    const { data } = await api.post('/subscriptions', subscription);
    return data;
  },

  update: async (id: number, subscription: Partial<SubscriptionCreate>) => {
    const { data } = await api.put(`/subscriptions/${id}`, subscription);
    return data;
  },

  delete: async (id: number) => {
    await api.delete(`/subscriptions/${id}`);
  },
};
```

### 8.3 Core Components

**File**: `frontend/src/components/common/Card.tsx`
```typescript
import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;
}

export const Card: React.FC<CardProps> = ({ children, className = '', hover = false }) => {
  return (
    <div className={`card ${hover ? 'hover:shadow-lg' : ''} ${className}`}>
      {children}
    </div>
  );
};
```

**File**: `frontend/src/components/subscriptions/SubscriptionCard.tsx`
```typescript
import React from 'react';
import { Subscription } from '../../types';
import { Card } from '../common/Card';
import { Calendar, DollarSign, Edit2, Trash2 } from 'lucide-react';

interface SubscriptionCardProps {
  subscription: Subscription;
  onEdit: (id: number) => void;
  onDelete: (id: number) => void;
}

export const SubscriptionCard: React.FC<SubscriptionCardProps> = ({
  subscription,
  onEdit,
  onDelete,
}) => {
  return (
    <Card hover className="subscription-card">
      <div className="flex items-start justify-between">
        <div className="flex items-center gap-4">
          {subscription.logo && (
            <img
              src={`/uploads/logos/${subscription.logo}`}
              alt={subscription.name}
              className="w-12 h-12 rounded-lg object-cover"
            />
          )}
          <div>
            <h3 className="text-lg font-semibold text-text-primary">
              {subscription.name}
            </h3>
            {subscription.category && (
              <span className="text-sm text-text-secondary">
                {subscription.category.name}
              </span>
            )}
          </div>
        </div>

        <div className="flex gap-2">
          <button
            onClick={() => onEdit(subscription.id)}
            className="p-2 hover:bg-bg-icon rounded-lg transition"
          >
            <Edit2 size={16} className="text-text-secondary" />
          </button>
          <button
            onClick={() => onDelete(subscription.id)}
            className="p-2 hover:bg-red-50 rounded-lg transition"
          >
            <Trash2 size={16} className="text-red-500" />
          </button>
        </div>
      </div>

      <div className="mt-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <DollarSign size={16} className="text-accent" />
          <span className="text-xl font-bold text-text-primary">
            {subscription.currency.symbol}{subscription.price.toFixed(2)}
          </span>
          <span className="text-sm text-text-secondary">
            /{subscription.cycle === 3 ? 'month' : 'year'}
          </span>
        </div>

        <div className="flex items-center gap-2 text-text-secondary">
          <Calendar size={16} />
          <span className="text-sm">
            Next: {new Date(subscription.next_payment).toLocaleDateString()}
          </span>
        </div>
      </div>
    </Card>
  );
};
```

**File**: `frontend/src/pages/DashboardPage.tsx`
```typescript
import React from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../services/api';
import { Card } from '../components/common/Card';
import { DollarSign, CreditCard, TrendingUp, Calendar } from 'lucide-react';

export const DashboardPage: React.FC = () => {
  const { data: overview } = useQuery(['dashboard-overview'], async () => {
    const { data } = await api.get('/stats/overview');
    return data.data;
  });

  const { data: budget } = useQuery(['budget'], async () => {
    const { data } = await api.get('/budget');
    return data.data;
  });

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-text-primary mb-8">Dashboard</h1>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <Card>
          <div className="flex items-center gap-4">
            <div className="p-3 bg-bg-icon rounded-lg">
              <CreditCard className="text-accent" size={24} />
            </div>
            <div>
              <p className="text-sm text-text-secondary">Active Subscriptions</p>
              <p className="text-2xl font-bold text-text-primary">
                {overview?.total_active || 0}
              </p>
            </div>
          </div>
        </Card>

        <Card>
          <div className="flex items-center gap-4">
            <div className="p-3 bg-bg-icon rounded-lg">
              <DollarSign className="text-accent" size={24} />
            </div>
            <div>
              <p className="text-sm text-text-secondary">Monthly Cost</p>
              <p className="text-2xl font-bold text-text-primary">
                ${budget?.current_spending?.toFixed(2) || '0.00'}
              </p>
            </div>
          </div>
        </Card>

        <Card>
          <div className="flex items-center gap-4">
            <div className="p-3 bg-bg-icon rounded-lg">
              <TrendingUp className="text-accent" size={24} />
            </div>
            <div>
              <p className="text-sm text-text-secondary">Budget Usage</p>
              <p className="text-2xl font-bold text-text-primary">
                {budget?.utilization?.toFixed(1) || '0'}%
              </p>
            </div>
          </div>
        </Card>

        <Card>
          <div className="flex items-center gap-4">
            <div className="p-3 bg-bg-icon rounded-lg">
              <Calendar className="text-accent" size={24} />
            </div>
            <div>
              <p className="text-sm text-text-secondary">Upcoming Payments</p>
              <p className="text-2xl font-bold text-text-primary">
                {overview?.upcoming_count || 0}
              </p>
            </div>
          </div>
        </Card>
      </div>

      {/* Upcoming Payments */}
      <Card className="mb-8">
        <h2 className="text-xl font-semibold text-text-primary mb-4">
          Upcoming Payments (Next 7 Days)
        </h2>
        <div className="space-y-3">
          {overview?.upcoming_payments?.map((payment: any) => (
            <div
              key={payment.id}
              className="flex items-center justify-between p-4 bg-bg-main rounded-lg"
            >
              <div className="flex items-center gap-3">
                {payment.logo && (
                  <img
                    src={`/uploads/logos/${payment.logo}`}
                    alt={payment.name}
                    className="w-10 h-10 rounded-lg"
                  />
                )}
                <div>
                  <p className="font-medium text-text-primary">{payment.name}</p>
                  <p className="text-sm text-text-secondary">
                    {new Date(payment.next_payment).toLocaleDateString()}
                  </p>
                </div>
              </div>
              <div className="text-right">
                <p className="font-semibold text-text-primary">
                  {payment.currency.symbol}{payment.price.toFixed(2)}
                </p>
              </div>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};
```

### Deliverables (Phase 6)
- ✅ React + TypeScript setup with Vite
- ✅ Integrations UI design system applied
- ✅ API client with interceptors
- ✅ Dashboard page
- ✅ Subscriptions page
- ✅ Calendar page
- ✅ Statistics page
- ✅ Insights page
- ✅ OCR upload page
- ✅ Settings page
- ✅ All reusable components
- ✅ Responsive design (mobile, tablet, desktop)

---

## 9. Phase 7: Testing & Deployment (Week 17-18)

### Objectives
- Unit and integration tests
- Docker containerization
- Documentation
- Launch script
- Production deployment

### 9.1 Testing

#### Step 7.1: Backend Tests

**File**: `backend/tests/conftest.py`
```python
import pytest
from app import create_app, db
from app.config import Config

class TestConfig(Config):
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'

@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(client):
    # Create user and login
    client.post('/api/v1/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })

    response = client.post('/api/v1/auth/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })

    token = response.json['token']
    return {'Authorization': f'Bearer {token}'}
```

**File**: `backend/tests/unit/test_billing_cycle.py`
```python
from datetime import datetime
from app.services.billing_cycle import BillingCycleCalculator

def test_calculate_next_payment_monthly():
    start = datetime(2025, 1, 15)
    next_payment = BillingCycleCalculator.calculate_next_payment(start, 3, 1)
    assert next_payment == datetime(2025, 2, 15)

def test_calculate_monthly_cost():
    # $30 every 3 months = $10/month
    monthly = BillingCycleCalculator.calculate_monthly_cost(30, 3, 3)
    assert monthly == 10.0
```

**File**: `backend/tests/integration/test_subscriptions_api.py`
```python
def test_create_subscription(client, auth_headers):
    response = client.post('/api/v1/subscriptions', json={
        'name': 'Netflix',
        'price': 15.99,
        'currency_id': 1,
        'cycle': 3,
        'frequency': 1
    }, headers=auth_headers)

    assert response.status_code == 201
    assert response.json['data']['name'] == 'Netflix'

def test_list_subscriptions(client, auth_headers):
    response = client.get('/api/v1/subscriptions', headers=auth_headers)
    assert response.status_code == 200
    assert 'data' in response.json
```

#### Step 7.2: Frontend Tests

```bash
cd frontend
npm install -D vitest @testing-library/react @testing-library/jest-dom
```

**File**: `frontend/src/components/__tests__/Card.test.tsx`
```typescript
import { render, screen } from '@testing-library/react';
import { Card } from '../common/Card';

describe('Card Component', () => {
  it('renders children correctly', () => {
    render(<Card>Test Content</Card>);
    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });
});
```

### 9.2 Docker Deployment (Optional but Recommended)

#### Step 7.3: Dockerfiles

**File**: `docker/Dockerfile.backend`
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ .

# Create uploads directory
RUN mkdir -p /app/uploads/logos /app/uploads/receipts

# Run migrations and start app
CMD alembic upgrade head && python run.py
```

**File**: `docker/Dockerfile.frontend`
```dockerfile
FROM node:18-alpine AS build

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ .
RUN npm run build

FROM nginx:alpine

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**File**: `docker/nginx.conf`
```nginx
server {
    listen 80;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    # Frontend
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API proxy
    location /api/ {
        proxy_pass http://backend:3038;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

**File**: `docker-compose.yml`
```yaml
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: docker/Dockerfile.backend
    container_name: subos-backend
    ports:
      - "3038:3038"
    environment:
      - DATABASE_URL=sqlite:///data/subos.db
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=False
    volumes:
      - ./data:/app/data
      - ./uploads:/app/uploads
    restart: unless-stopped

  frontend:
    build:
      context: .
      dockerfile: docker/Dockerfile.frontend
    container_name: subos-frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped
```

### 9.3 Startup Script (Without Docker)

**File**: `scripts/start.sh`
```bash
#!/bin/bash

# SubOS Quick Launcher Script
# Starts both backend and frontend servers

APP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PORT=3038

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting SubOS...${NC}"

# Backend
cd "$APP_DIR/backend"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Run migrations
echo -e "${YELLOW}Running database migrations...${NC}"
alembic upgrade head

# Start backend
echo -e "${GREEN}Starting backend server on port $PORT...${NC}"
python run.py &
BACKEND_PID=$!

# Frontend
cd "$APP_DIR/frontend"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}Installing frontend dependencies...${NC}"
    npm install
fi

# Start frontend
echo -e "${GREEN}Starting frontend server...${NC}"
npm run dev &
FRONTEND_PID=$!

# Wait for servers to start
sleep 5

# Open browser
echo -e "${GREEN}Opening browser...${NC}"
open http://localhost:5173

echo -e "${GREEN}✅ SubOS is running!${NC}"
echo -e "${YELLOW}Backend: http://localhost:$PORT${NC}"
echo -e "${YELLOW}Frontend: http://localhost:5173${NC}"
echo -e "${YELLOW}To stop: kill $BACKEND_PID $FRONTEND_PID${NC}"

# Wait for processes
wait $BACKEND_PID $FRONTEND_PID
```

**Make executable**:
```bash
chmod +x scripts/start.sh
```

### 9.4 Documentation

**File**: `README.md`
```markdown
# SubOS - Personal Subscription Manager

Self-hosted, privacy-first subscription management platform with AI-powered insights and OCR receipt processing.

## Features

- 📊 Track unlimited subscriptions with flexible billing cycles
- 💱 Multi-currency support with auto-updated exchange rates
- 💰 Budget tracking and spending analytics
- 🔔 9 notification channels (Email, Discord, Telegram, etc.)
- 🤖 AI-powered cost optimization recommendations
- 📸 OCR receipt processing for automatic data entry
- 📈 ML-powered insights and predictive analytics
- 🏠 Household member management
- 🔒 2FA authentication with TOTP
- 🎨 Clean, minimal UI with Integrations design system

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone <repo-url>
cd SubOS

# Copy environment file
cp .env.example .env
# Edit .env with your settings

# Start with Docker Compose
docker-compose up -d

# Access at http://localhost
```

### Option 2: Local Development

```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python run.py

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Access at http://localhost:5173

### Option 3: Quick Launch Script

```bash
./scripts/start.sh
```

## Technology Stack

- **Backend**: Flask + SQLAlchemy + SQLite
- **Frontend**: React + TypeScript + Vite
- **ML/AI**: scikit-learn, OpenAI, Google Gemini, Ollama
- **OCR**: Tesseract, Google Vision API
- **Notifications**: APScheduler + 9 channel integrations
- **Design**: Integrations UI (JetBrains Mono, clean minimal)

## Documentation

- [PRD.md](PRD.md) - Product Requirements Document
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) - Implementation Plan
- API Docs: http://localhost:3038/api/docs (when running)

## License

MIT

## Credits

Inspired by [Wallos](https://github.com/ellite/Wallos/)
```

### Deliverables (Phase 7)
- ✅ Backend unit tests (20+ tests)
- ✅ Backend integration tests (15+ tests)
- ✅ Frontend component tests (10+ tests)
- ✅ Docker setup (optional)
- ✅ docker-compose.yml
- ✅ Quick launch script
- ✅ Comprehensive README
- ✅ API documentation
- ✅ Production deployment guide

---

## 10. Technical Stack Details

### 10.1 Backend Dependencies

**File**: `backend/requirements.txt`
```
# Core Framework
flask==3.0.0
flask-cors==4.0.0
flask-sqlalchemy==3.1.1
sqlalchemy==2.0.23

# Database & Migrations
alembic==1.13.0

# Authentication & Security
bcrypt==4.1.2
pyjwt==2.8.0
pyotp==2.9.0
cryptography==41.0.7

# Task Scheduling
apscheduler==3.10.4

# API & Integrations
requests==2.31.0
python-telegram-bot==20.7
discord-webhook==1.3.0

# ML & AI
scikit-learn==1.3.2
pandas==2.1.4
numpy==1.26.2
statsmodels==0.14.1
prophet==1.1.5
openai==1.6.1
google-generativeai==0.3.2
ollama==0.1.6

# OCR
pytesseract==0.3.10
pillow==10.1.0
pdf2image==1.16.3
google-cloud-vision==3.5.0
opencv-python==4.8.1.78

# Utilities
python-dotenv==1.0.0
python-dateutil==2.8.2
qrcode==7.4.2
```

### 10.2 Frontend Dependencies

**File**: `frontend/package.json`
```json
{
  "name": "subos-frontend",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.1",
    "@tanstack/react-query": "^5.14.2",
    "axios": "^1.6.2",
    "chart.js": "^4.4.1",
    "react-chartjs-2": "^5.2.0",
    "date-fns": "^3.0.6",
    "react-hook-form": "^7.49.2",
    "zod": "^3.22.4",
    "@hookform/resolvers": "^3.3.3",
    "lucide-react": "^0.300.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.2.0",
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.3.3",
    "vite": "^5.0.8",
    "tailwindcss": "^3.4.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "vitest": "^1.0.4",
    "@testing-library/react": "^14.1.2",
    "@testing-library/jest-dom": "^6.1.5"
  }
}
```

---

## 11. Deployment Options

### 11.1 Docker Deployment (Production)

**Advantages**:
- Isolated environment
- Easy updates
- Consistent across systems
- Single-command deployment

**Steps**:
```bash
# 1. Build and start
docker-compose up -d

# 2. View logs
docker-compose logs -f

# 3. Stop
docker-compose down

# 4. Update
git pull
docker-compose down
docker-compose build
docker-compose up -d
```

### 11.2 Bare Metal Deployment

**Advantages**:
- Direct system access
- Easier debugging during development
- No Docker overhead

**Steps**:
```bash
# 1. Install dependencies
python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt

cd frontend
npm install

# 2. Configure environment
cp .env.example .env
# Edit .env

# 3. Run migrations
cd backend
alembic upgrade head

# 4. Start with process manager (PM2, systemd, etc.)
pm2 start ecosystem.config.js
```

### 11.3 Cloud Deployment

**Recommended Platforms**:
- **Railway**: Easy deployment, auto-scaling
- **Fly.io**: Global CDN, edge deployment
- **DigitalOcean App Platform**: Simple PaaS
- **AWS EC2 + RDS**: Full control, scalable

---

## 12. Testing Strategy

### 12.1 Backend Testing

**Unit Tests**:
- Models (validation, relationships)
- Services (business logic)
- Utilities (date calculations, encryption)

**Integration Tests**:
- API endpoints (CRUD operations)
- Authentication flow
- Notification delivery
- OCR processing

**Coverage Target**: 80%+

### 12.2 Frontend Testing

**Component Tests**:
- UI components render correctly
- User interactions work
- Forms validate properly

**Integration Tests**:
- API calls succeed
- State management works
- Routing functions

**Coverage Target**: 70%+

### 12.3 End-to-End Testing

**Critical Flows**:
- User registration → login → add subscription
- Budget setup → view analytics
- Upload receipt → OCR → create subscription
- Configure notifications → receive alerts

**Tool**: Playwright or Cypress

---

## Summary

This implementation plan provides a comprehensive 18-week roadmap to build SubOS from foundation to production. The plan includes:

✅ **7 Development Phases**
✅ **Complete Tech Stack** (Python, React, SQLite, ML, OCR)
✅ **Full Feature Parity** with Wallos
✅ **Enhanced Features** (ML Insights, OCR)
✅ **Integrations UI Design System** (Clean, minimal, JetBrains Mono)
✅ **Flexible Deployment** (Docker or bare metal)
✅ **Comprehensive Testing**
✅ **Production-Ready Documentation**

**Port**: 3038
**Timeline**: 18 weeks
**Team Size**: 1-2 developers

Each phase builds upon the previous, with clear deliverables and testing checkpoints. The modular architecture allows for parallel development of backend and frontend features.

---

**Next Steps**:
1. Review and approve this implementation plan
2. Set up development environment
3. Begin Phase 1: Foundation (Week 1-2)
4. Establish weekly sprint reviews
5. Track progress against milestones

**Contact**: For questions or clarifications, refer to PRD.md or open a discussion.
