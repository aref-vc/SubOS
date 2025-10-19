# SubOS - Personal Subscription Manager
## Product Requirements Document (PRD)

**Version**: 1.0
**Date**: October 19, 2025
**Status**: Draft
**Author**: Product Team
**Port Allocation**: 3038

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Overview](#product-overview)
3. [Target Users](#target-users)
4. [Core Features](#core-features)
5. [Enhanced Features](#enhanced-features)
6. [Technical Architecture](#technical-architecture)
7. [Database Schema](#database-schema)
8. [API Specifications](#api-specifications)
9. [UI/UX Requirements](#uiux-requirements)
10. [Security & Privacy](#security--privacy)
11. [Integration Requirements](#integration-requirements)
12. [Success Metrics](#success-metrics)
13. [Future Roadmap](#future-roadmap)

---

## 1. Executive Summary

### Vision
SubOS is a self-hosted, privacy-first subscription management platform that empowers users to track recurring expenses, optimize spending, and gain intelligent insights into their subscription portfolio. Inspired by Wallos, SubOS extends the foundation with ML-powered analytics and automated data entry through receipt OCR.

### Key Objectives
- **Complete Subscription Visibility**: Centralized tracking of all recurring subscriptions
- **Financial Intelligence**: AI-powered insights and spending optimization recommendations
- **Privacy & Ownership**: Self-hosted solution with complete data control
- **Automation**: Reduce manual data entry through OCR and AI-assisted workflows
- **Multi-Currency Support**: Global usage with real-time currency conversion
- **Comprehensive Notifications**: Never miss a payment with 9 notification channels

### Success Criteria
- Users reduce subscription waste by 15-30% within 3 months
- 95% of subscriptions automatically detected via OCR or AI
- Zero missed payments through reliable notification system
- Sub-second response times for all dashboard views
- 100% data privacy with local-only storage option

---

## 2. Product Overview

### 2.1 Product Description
SubOS is an open-source, self-hostable web application built with Python (Flask/FastAPI) and SQLite, designed to help individuals and households manage recurring subscriptions, track spending patterns, and optimize costs through intelligent recommendations.

### 2.2 Inspiration
Based on the successful Wallos project (6,173 GitHub stars), SubOS maintains feature parity while extending capabilities with:
- **Smart Insights Dashboard**: ML-powered spending pattern analysis
- **Receipt OCR**: Automated subscription data entry from receipts/invoices
- **Enhanced Analytics**: Predictive budgeting and anomaly detection

### 2.3 Deployment Model
- **Primary**: Docker containerization with single-command deployment
- **Alternative**: Bare-metal installation with Python virtual environment
- **Port**: 3038 (Backend API + Frontend)
- **Database**: SQLite (single-file, portable)

---

## 3. Target Users

### 3.1 Primary Personas

#### **Persona 1: Budget-Conscious Professional**
- **Demographics**: 25-45, tech-savvy, tracks personal finances
- **Needs**: Visibility into subscription costs, budget adherence, cost optimization
- **Pain Points**: Forgotten trials, unused subscriptions, surprise charges
- **Goals**: Reduce monthly expenses by 20%, eliminate waste

#### **Persona 2: Privacy Advocate**
- **Demographics**: 30-50, values data ownership, self-hosting enthusiast
- **Needs**: Complete data control, no external dependencies, open-source
- **Pain Points**: Distrust of cloud-based finance apps, data breaches
- **Goals**: Full privacy, local-only processing, audit trail

#### **Persona 3: Household Manager**
- **Demographics**: Family manager tracking household subscriptions
- **Needs**: Multi-member tracking, shared budget visibility, notifications
- **Pain Points**: Duplicate subscriptions, lack of centralized tracking
- **Goals**: Household budget optimization, transparent expense sharing

### 3.2 Use Cases

**UC-1: Track Personal Subscriptions**
User adds Netflix, Spotify, Amazon Prime to SubOS, receives payment reminders, views monthly cost dashboard.

**UC-2: Budget Management**
User sets $150/month subscription budget, receives alerts when approaching limit, gets AI recommendations to optimize.

**UC-3: OCR Receipt Processing**
User receives Apple receipt email, uploads to SubOS, OCR auto-extracts subscription details and creates entry.

**UC-4: Multi-Currency Management**
User has subscriptions in USD, EUR, GBP, converts all to primary currency for unified budget view.

**UC-5: Household Tracking**
Family tracks Netflix (Dad), Disney+ (Mom), YouTube Premium (Kids), sets per-member budgets.

---

## 4. Core Features

### 4.1 Subscription Management

#### 4.1.1 CRUD Operations
- **Create**: Add subscriptions with rich metadata
- **Read**: List, search, filter subscriptions
- **Update**: Edit details, change billing cycles, update costs
- **Delete**: Remove subscriptions, mark as inactive

#### 4.1.2 Subscription Attributes
- **Basic Info**:
  - Name (required)
  - Logo (upload or web search)
  - URL (optional)
  - Notes (rich text)

- **Billing Details**:
  - Price (decimal, 2 places)
  - Currency (from currency table)
  - Billing Cycle: Days/Weeks/Months/Years
  - Frequency: 1-366 units (e.g., "every 2 months")
  - Next Payment Date (auto-calculated)
  - Auto-Renewal: Yes/No

- **Organization**:
  - Category (user-defined)
  - Payment Method (user-defined)
  - Payer (household member)

- **Lifecycle**:
  - Active/Inactive status
  - Cancellation date (if inactive)
  - Replacement subscription ID (if switched)

#### 4.1.3 Billing Cycle Engine
- **Supported Cycles**:
  - Daily (1-366 days)
  - Weekly (1-52 weeks)
  - Monthly (1-12 months)
  - Yearly (1-10 years)

- **Calculation Logic**:
  - Auto-calculate next payment date on creation
  - Update on manual renewal confirmation
  - Handle leap years, month-end edge cases
  - Timezone-aware date handling

### 4.2 Multi-Currency Support

#### 4.2.1 Currency Management
- **System Currencies**: Pre-loaded USD, EUR, GBP, JPY, etc.
- **Custom Currencies**: User-defined currencies with custom symbols
- **Exchange Rates**:
  - Integration with Fixer.io API
  - Daily auto-update via cron job (2:00 AM)
  - Historical rate storage for trend analysis

#### 4.2.2 Currency Conversion
- **Display Options**:
  - Show original price
  - Show converted price in main currency
  - Show both original + converted

- **Conversion Logic**:
  - Real-time conversion using latest rates
  - Conversion rate stored with subscription for audit
  - Recalculate totals when rates update

### 4.3 Budget Management

#### 4.3.1 Budget Configuration
- **Monthly Budget**: User-defined target amount
- **Multi-Member Budgets**: Individual budgets per household member
- **Budget Period**: Monthly (with yearly projection)

#### 4.3.2 Budget Tracking
- **Calculations**:
  - Total monthly cost (sum of all active subscriptions)
  - Budget utilization percentage
  - Projected yearly cost
  - Savings from inactive subscriptions

- **Alerts**:
  - Warning at 80% budget utilization
  - Critical alert at 100% budget
  - Trend alerts (spending increasing >10% month-over-month)

### 4.4 Notification System

#### 4.4.1 Notification Channels (9 Total)

1. **Email (SMTP)**
   - Configuration: SMTP server, port, credentials
   - Templates: Upcoming payment, cancellation reminder, overdue renewal

2. **Discord**
   - Webhook URL configuration
   - Rich embed formatting

3. **Telegram**
   - Bot token + Chat ID
   - Inline keyboard actions

4. **Pushover**
   - User key + API token
   - Priority levels

5. **PushPlus**
   - Token-based authentication

6. **Mattermost**
   - Webhook integration

7. **Ntfy**
   - Topic-based notifications

8. **Gotify**
   - Self-hosted push server

9. **Generic Webhook**
   - Custom URL with template variables
   - Configurable payload structure

#### 4.4.2 Notification Types
- **Upcoming Payment**: N days before next payment (user-configurable)
- **Cancellation Reminder**: Notify before subscription auto-renews
- **Overdue Manual Renewal**: Payment date passed without confirmation
- **Budget Alerts**: Approaching or exceeding budget

#### 4.4.3 Notification Configuration
- **Global Settings**: Default days before payment (7 days)
- **Per-Subscription Override**: Custom notification timing
- **Per-Member Settings**: Each household member gets their own notifications
- **Channel Routing**: Different notification types to different channels

#### 4.4.4 Notification Scheduling
- **Cron Jobs**:
  - Daily scan at 9:00 AM for upcoming payments
  - Daily scan at 8:00 AM for cancellations
  - Email queue processing every 2 minutes

### 4.5 Household & Multi-Member Management

#### 4.5.1 Household Members
- **Member Attributes**:
  - Name
  - Email (for notifications)
  - Avatar/Icon

- **Member Management**:
  - Add/edit/remove household members
  - Assign subscriptions to members
  - View per-member spending

#### 4.5.2 Shared Visibility
- **Dashboard Views**:
  - Household total spending
  - Per-member breakdown
  - Shared vs individual subscriptions

- **Notifications**:
  - Members receive notifications for their subscriptions
  - Admin receives all notifications

### 4.6 Categories & Payment Methods

#### 4.6.1 Categories
- **System Categories**: Entertainment, Productivity, Cloud Storage, etc.
- **Custom Categories**: User-defined with custom names
- **Category Attributes**:
  - Name
  - Order (drag-to-reorder)

#### 4.6.2 Payment Methods
- **Common Methods**: Credit Card, Debit Card, PayPal, Bank Transfer
- **Custom Methods**: User-defined
- **Attributes**:
  - Name
  - Icon (from icon library)
  - Order

### 4.7 Authentication & User Management

#### 4.7.1 Multi-User Support
- **User Roles**:
  - Admin: System-wide settings, user management
  - Regular User: Own subscriptions, household members

#### 4.7.2 Authentication Methods

**Local Authentication**:
- Username/password with bcrypt hashing
- Email verification workflow
- Password reset via email tokens
- Session-based authentication

**TOTP 2FA**:
- QR code generation for authenticator apps
- Backup codes generation
- Enforced 2FA for admin users

**OAuth/OIDC**:
- Configurable OAuth providers (Google, GitHub, etc.)
- Admin-controlled enablement
- Automatic user provisioning
- Attribute mapping

#### 4.7.3 Session Management
- Secure session cookies (HttpOnly, SameSite)
- Session timeout (30-day default, configurable)
- Remember me functionality
- Device tracking and session revocation

### 4.8 Logo Management

#### 4.8.1 Logo Upload
- File upload (PNG, JPG, SVG)
- Max size: 2MB
- Auto-resize to 256x256
- Image optimization

#### 4.8.2 Logo Web Search
- Integration with logo search services
- Search by subscription name
- Preview before selection
- Fallback to default icons

#### 4.8.3 Logo Storage
- Local filesystem storage
- Organized by subscription ID
- Thumbnail generation

### 4.9 AI-Powered Features

#### 4.9.1 Cost Optimization Recommendations
- **AI Models Supported**:
  - OpenAI ChatGPT (GPT-4)
  - Google Gemini
  - Local Ollama (privacy-focused)

#### 4.9.2 Recommendation Types
- **Duplicate Detection**: Identify overlapping services
- **Alternative Suggestions**: Cheaper alternatives to current subscriptions
- **Bundle Opportunities**: Suggest bundle deals
- **Cancellation Recommendations**: Unused/underutilized subscriptions
- **Upgrade/Downgrade**: Optimize plan tiers

#### 4.9.3 AI Recommendation Workflow
1. User triggers analysis (manual or scheduled)
2. System sends anonymized subscription data to AI
3. AI returns structured recommendations
4. Recommendations stored in database
5. User can dismiss or act on recommendations

### 4.10 Statistics & Analytics

#### 4.10.1 Dashboard Overview
- **Key Metrics**:
  - Total active subscriptions
  - Monthly total cost
  - Yearly projected cost
  - Budget utilization
  - Savings from inactive subscriptions

#### 4.10.2 Analytics Views

**Spending Trends**:
- Monthly spending over time (line chart)
- Year-over-year comparison
- Category breakdown (pie chart)

**Subscription Health**:
- Upcoming payments (next 7 days)
- Overdue manual renewals
- Recently added subscriptions

**Category Analysis**:
- Cost per category (bar chart)
- Subscription count per category
- Category trends

**Payment Method Analysis**:
- Cost per payment method
- Distribution chart

**Member Analysis**:
- Cost per household member
- Member comparison chart

#### 4.10.3 Exportable Reports
- CSV export of all subscriptions
- Monthly spending reports
- Yearly summary reports

### 4.11 Calendar View

#### 4.11.1 Calendar Features
- Monthly grid view
- Payment dates highlighted
- Click to view subscription details
- Filter by category/member/payment method

#### 4.11.2 Calendar Interactions
- Navigate months/years
- Export to iCal format
- Print-friendly view

### 4.12 Inactive Subscription Tracking

#### 4.12.1 Inactive Subscriptions
- **Attributes**:
  - Cancellation date
  - Reason for cancellation (optional)
  - Replacement subscription (if switched)
  - Final cost before cancellation

#### 4.12.2 Savings Calculation
- Track monthly savings from cancellations
- Project yearly savings
- Show savings trend over time

---

## 5. Enhanced Features

### 5.1 Smart Insights Dashboard

#### 5.1.1 ML-Powered Spending Analysis

**Spending Pattern Detection**:
- Identify weekly, monthly, quarterly patterns
- Seasonal subscription trends
- Unusual spending spikes
- Category preference analysis

**Predictive Budgeting**:
- Forecast next month's subscription costs
- Predict budget overruns
- Recommend budget adjustments
- Confidence intervals for predictions

**Anomaly Detection**:
- Detect unusual subscription additions
- Flag price changes
- Identify forgotten trials converting to paid
- Alert on duplicate subscriptions

#### 5.1.2 Intelligent Recommendations

**Personalized Insights**:
- "You spend 45% on entertainment - consider consolidation"
- "Netflix price increased by $2 last month"
- "You have 3 cloud storage subscriptions - opportunity to save $15/mo"
- "Spotify family plan would save you $8/mo"

**Optimization Opportunities**:
- Bundle suggestions
- Plan tier optimizations
- Annual vs monthly billing savings
- Unused subscription detection (no usage data integration)

#### 5.1.3 ML Models

**Clustering Algorithm**:
- K-means clustering for subscription grouping
- Identify similar spending patterns
- Segment subscriptions by usage patterns

**Time Series Forecasting**:
- ARIMA model for cost predictions
- Prophet for seasonal trend analysis
- Rolling average smoothing

**Anomaly Detection**:
- Isolation Forest for outlier detection
- Statistical threshold-based alerts
- Change point detection

#### 5.1.4 Dashboard Visualizations
- Spending heatmap (calendar-based)
- Forecast vs actual spending
- Category spending evolution
- Predictive budget gauge
- Anomaly timeline

### 5.2 Receipt OCR

#### 5.2.1 OCR Engine Options

**Tesseract OCR (Local)**:
- Open-source, privacy-focused
- No external API dependency
- Supports 100+ languages
- Image preprocessing for accuracy

**Google Vision API (Cloud)**:
- Higher accuracy (95%+)
- Handwriting recognition
- Multi-language detection
- API key required

#### 5.2.2 Supported Input Methods
- **File Upload**: PNG, JPG, PDF receipts
- **Email Forward**: Forward receipt emails to SubOS
- **Mobile Capture**: Take photo of physical receipt
- **Screenshot Paste**: Paste screenshot from clipboard

#### 5.2.3 OCR Processing Pipeline

**Step 1: Image Preprocessing**
- Grayscale conversion
- Noise reduction
- Contrast enhancement
- Skew correction
- Binarization

**Step 2: Text Extraction**
- OCR engine processing
- Text block detection
- Confidence scoring

**Step 3: Data Parsing**
- **Subscription Name**: Extract service name
- **Price**: Detect amount and currency
- **Billing Date**: Parse payment date
- **Billing Cycle**: Infer from "monthly", "annual", etc.
- **Email/URL**: Extract contact info

**Step 4: Entity Recognition**
- NLP-based entity extraction
- Subscription brand recognition
- Currency code detection
- Date normalization

**Step 5: Auto-Fill**
- Pre-populate subscription form
- User reviews and confirms
- Option to auto-save or manual edit

#### 5.2.4 OCR Accuracy Enhancement
- **Template Matching**: Pre-configured templates for popular services (Netflix, Spotify, etc.)
- **Learning from Corrections**: User edits improve future OCR
- **Confidence Thresholds**: Flag low-confidence extractions for review
- **Multi-Format Support**: Handle different receipt layouts

#### 5.2.5 Receipt Storage
- Original receipt image stored
- Extracted text stored as JSON
- Linked to subscription record
- Searchable receipt archive

---

## 6. Technical Architecture

### 6.1 Technology Stack

#### Backend
- **Framework**: Flask (lightweight) or FastAPI (async, modern)
- **ORM**: SQLAlchemy 2.0
- **Database**: SQLite 3 (with WAL mode for concurrency)
- **Task Scheduler**: APScheduler for cron jobs
- **Session Management**: Flask-Login or FastAPI sessions
- **Authentication**: Flask-Security-Too or custom JWT
- **API Documentation**: Swagger/OpenAPI (auto-generated)

#### ML & AI
- **ML Framework**: scikit-learn (for clustering, anomaly detection)
- **Time Series**: statsmodels (ARIMA), Prophet
- **OCR**: Tesseract (pytesseract) or Google Vision API
- **NLP**: spaCy for entity recognition
- **AI Integration**: OpenAI API, Google Gemini API, Ollama client

#### Frontend
- **Framework**: React 18 with TypeScript
- **State Management**: React Context + Hooks or Zustand
- **UI Library**: Tailwind CSS + shadcn/ui components
- **Charts**: Chart.js or Plotly.js
- **Icons**: Lucide React or Material Icons
- **Forms**: React Hook Form + Zod validation

#### Deployment
- **Containerization**: Docker + Docker Compose
- **Web Server**: NGINX (reverse proxy)
- **Process Manager**: Gunicorn or Uvicorn
- **Database**: SQLite (persistent volume)
- **Logging**: Python logging to file + console

### 6.2 System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  User Interface                     │
│              (React + TypeScript)                   │
└───────────────────┬─────────────────────────────────┘
                    │ HTTPS (Port 3038)
                    ▼
┌─────────────────────────────────────────────────────┐
│                 NGINX Reverse Proxy                 │
│            (SSL Termination, Static Files)          │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Flask/FastAPI Application              │
│  ┌─────────────────────────────────────────────┐   │
│  │          REST API Endpoints                 │   │
│  ├─────────────────────────────────────────────┤   │
│  │    Authentication  │  Subscriptions         │   │
│  │    Notifications   │  Budgets               │   │
│  │    AI Insights     │  OCR Processing        │   │
│  └─────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────┐   │
│  │           Business Logic Layer              │   │
│  │  - Billing Cycle Calculator                 │   │
│  │  - Currency Converter                       │   │
│  │  - Budget Analyzer                          │   │
│  │  - ML Insights Engine                       │   │
│  │  - OCR Pipeline                             │   │
│  └─────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────┐   │
│  │           Data Access Layer (ORM)           │   │
│  │              SQLAlchemy Models              │   │
│  └─────────────────────────────────────────────┘   │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│               SQLite Database                       │
│  - subscriptions.db (main database)                 │
│  - WAL mode enabled for concurrency                 │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│              Background Services                    │
│  ┌──────────────┐  ┌──────────────┐                │
│  │  APScheduler │  │ Notification │                │
│  │  Cron Jobs   │  │   Workers    │                │
│  │              │  │              │                │
│  │ - Currency   │  │ - Email      │                │
│  │   Updates    │  │ - Webhooks   │                │
│  │ - Payment    │  │ - Push       │                │
│  │   Reminders  │  │   Services   │                │
│  └──────────────┘  └──────────────┘                │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│            External Integrations                    │
│  - Fixer.io API (Currency Rates)                   │
│  - OpenAI/Gemini/Ollama (AI Recommendations)        │
│  - Google Vision API / Tesseract (OCR)             │
│  - SMTP Server (Email Notifications)               │
│  - Webhook Endpoints (Discord, Telegram, etc.)     │
└─────────────────────────────────────────────────────┘
```

### 6.3 Data Flow

#### Subscription Creation Flow
```
User Input → Frontend Validation → API Request →
Backend Validation → Currency Conversion →
Next Payment Calculation → Database Insert →
Logo Processing → Response to Frontend
```

#### Notification Flow
```
Cron Job Trigger → Query Upcoming Payments →
For Each Subscription → Check Notification Settings →
Format Message → Send to Channel(s) →
Log Notification → Update Status
```

#### OCR Flow
```
Receipt Upload → Image Preprocessing →
OCR Engine Processing → Text Extraction →
Entity Recognition (NLP) → Field Mapping →
Auto-Fill Form → User Review → Confirmation →
Subscription Creation + Receipt Storage
```

#### ML Insights Flow
```
Trigger Analysis → Load Historical Data →
Feature Engineering → Model Prediction →
Anomaly Detection → Pattern Recognition →
Generate Insights → Store Recommendations →
Display on Dashboard
```

---

## 7. Database Schema

### 7.1 Entity-Relationship Diagram

```
┌──────────────┐       ┌────────────────┐       ┌──────────────┐
│    users     │       │  subscriptions │       │  currencies  │
├──────────────┤       ├────────────────┤       ├──────────────┤
│ id (PK)      │◄──────┤ user_id (FK)   │       │ id (PK)      │
│ username     │       │ name           │───────► currency_id  │
│ password     │       │ price          │       │ code         │
│ email        │       │ cycle          │       │ symbol       │
│ ...          │       │ next_payment   │       │ rate         │
└──────────────┘       └────────────────┘       └──────────────┘
                              │
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐       ┌────────────────┐   ┌──────────────┐
│  categories  │       │   household    │   │payment_methods│
├──────────────┤       ├────────────────┤   ├──────────────┤
│ id (PK)      │       │ id (PK)        │   │ id (PK)      │
│ user_id (FK) │       │ user_id (FK)   │   │ user_id (FK) │
│ name         │       │ name           │   │ name         │
└──────────────┘       └────────────────┘   └──────────────┘
```

### 7.2 Table Definitions

#### users
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,  -- bcrypt hash
    email TEXT UNIQUE NOT NULL,
    firstname TEXT,
    main_currency INTEGER,  -- FK to currencies
    budget REAL,
    avatar TEXT,  -- filename
    is_admin BOOLEAN DEFAULT 0,
    totp_secret TEXT,  -- for 2FA
    totp_enabled BOOLEAN DEFAULT 0,
    email_verified BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### subscriptions
```sql
CREATE TABLE subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    currency_id INTEGER NOT NULL,
    cycle INTEGER NOT NULL,  -- 1=days, 2=weeks, 3=months, 4=years
    frequency INTEGER NOT NULL DEFAULT 1,  -- every N cycles
    next_payment DATE,
    auto_renew BOOLEAN DEFAULT 1,
    logo TEXT,  -- filename
    url TEXT,
    notes TEXT,
    category_id INTEGER,
    payer_user_id INTEGER,  -- household member ID
    payment_method_id INTEGER,
    inactive BOOLEAN DEFAULT 0,
    cancellation_date DATE,
    replacement_subscription_id INTEGER,  -- FK to subscriptions
    notify_days_before INTEGER DEFAULT 7,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (currency_id) REFERENCES currencies(id),
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL,
    FOREIGN KEY (payer_user_id) REFERENCES household(id) ON DELETE SET NULL,
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id) ON DELETE SET NULL,
    FOREIGN KEY (replacement_subscription_id) REFERENCES subscriptions(id)
);

CREATE INDEX idx_subscriptions_user_id ON subscriptions(user_id);
CREATE INDEX idx_subscriptions_next_payment ON subscriptions(next_payment);
CREATE INDEX idx_subscriptions_inactive ON subscriptions(inactive);
```

#### currencies
```sql
CREATE TABLE currencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    code TEXT NOT NULL,  -- USD, EUR, GBP
    symbol TEXT NOT NULL,  -- $, €, £
    rate REAL NOT NULL DEFAULT 1.0,  -- exchange rate to USD
    last_updated TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_currencies_user_id ON currencies(user_id);
CREATE UNIQUE INDEX idx_currencies_user_code ON currencies(user_id, code);
```

#### categories
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    "order" INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_categories_user_id ON categories(user_id);
```

#### household
```sql
CREATE TABLE household (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    avatar TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_household_user_id ON household(user_id);
```

#### payment_methods
```sql
CREATE TABLE payment_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    icon TEXT,
    "order" INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_payment_methods_user_id ON payment_methods(user_id);
```

#### notification_settings
```sql
CREATE TABLE notification_settings (
    user_id INTEGER PRIMARY KEY,
    days_before INTEGER DEFAULT 7,
    email_enabled BOOLEAN DEFAULT 0,
    discord_enabled BOOLEAN DEFAULT 0,
    telegram_enabled BOOLEAN DEFAULT 0,
    pushover_enabled BOOLEAN DEFAULT 0,
    pushplus_enabled BOOLEAN DEFAULT 0,
    mattermost_enabled BOOLEAN DEFAULT 0,
    ntfy_enabled BOOLEAN DEFAULT 0,
    gotify_enabled BOOLEAN DEFAULT 0,
    webhook_enabled BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### email_notifications
```sql
CREATE TABLE email_notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    smtp_host TEXT NOT NULL,
    smtp_port INTEGER NOT NULL DEFAULT 587,
    smtp_username TEXT NOT NULL,
    smtp_password TEXT NOT NULL,  -- encrypted
    from_email TEXT NOT NULL,
    use_tls BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### discord_notifications
```sql
CREATE TABLE discord_notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    webhook_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### telegram_notifications
```sql
CREATE TABLE telegram_notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    bot_token TEXT NOT NULL,
    chat_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### pushover_notifications
```sql
CREATE TABLE pushover_notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_key TEXT NOT NULL,
    api_token TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### webhook_notifications
```sql
CREATE TABLE webhook_notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    webhook_url TEXT NOT NULL,
    payload_template TEXT,  -- JSON template with variables
    headers TEXT,  -- JSON object
    method TEXT DEFAULT 'POST',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### ai_recommendations
```sql
CREATE TABLE ai_recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    savings TEXT,
    recommendation_type TEXT,  -- duplicate, alternative, bundle, cancel, optimize
    related_subscription_ids TEXT,  -- JSON array
    dismissed BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_ai_recommendations_user_id ON ai_recommendations(user_id);
CREATE INDEX idx_ai_recommendations_dismissed ON ai_recommendations(dismissed);
```

#### receipts
```sql
CREATE TABLE receipts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subscription_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    filename TEXT NOT NULL,  -- original receipt image
    extracted_text TEXT,  -- full OCR text
    extracted_data TEXT,  -- JSON of parsed fields
    confidence_score REAL,
    ocr_provider TEXT,  -- tesseract or google_vision
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_receipts_subscription_id ON receipts(subscription_id);
CREATE INDEX idx_receipts_user_id ON receipts(user_id);
```

#### ml_insights
```sql
CREATE TABLE ml_insights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    insight_type TEXT NOT NULL,  -- anomaly, pattern, prediction, recommendation
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    data TEXT,  -- JSON with insight details
    severity TEXT,  -- info, warning, critical
    dismissed BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_ml_insights_user_id ON ml_insights(user_id);
CREATE INDEX idx_ml_insights_type ON ml_insights(insight_type);
```

#### notification_log
```sql
CREATE TABLE notification_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    subscription_id INTEGER,
    channel TEXT NOT NULL,  -- email, discord, etc.
    notification_type TEXT NOT NULL,  -- upcoming, cancellation, overdue
    status TEXT NOT NULL,  -- sent, failed
    error_message TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id) ON DELETE CASCADE
);

CREATE INDEX idx_notification_log_user_id ON notification_log(user_id);
CREATE INDEX idx_notification_log_sent_at ON notification_log(sent_at);
```

#### migrations
```sql
CREATE TABLE migrations (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 8. API Specifications

### 8.1 API Design Principles
- RESTful architecture
- JSON request/response format
- Semantic HTTP status codes
- Consistent error responses
- Versioned endpoints (v1)
- OpenAPI documentation

### 8.2 Authentication Endpoints

#### POST /api/v1/auth/register
**Description**: Register a new user
**Request Body**:
```json
{
  "username": "string (required)",
  "email": "string (required)",
  "password": "string (required, min 8 chars)",
  "firstname": "string (optional)"
}
```
**Response**: 201 Created
```json
{
  "status": "success",
  "message": "User registered successfully. Please verify your email.",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

#### POST /api/v1/auth/login
**Description**: Login with credentials
**Request Body**:
```json
{
  "username": "string",
  "password": "string",
  "totp_code": "string (optional, if 2FA enabled)"
}
```
**Response**: 200 OK
```json
{
  "status": "success",
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "username": "john_doe",
    "is_admin": false
  }
}
```

#### POST /api/v1/auth/logout
**Description**: Logout current session
**Response**: 200 OK

#### POST /api/v1/auth/forgot-password
**Description**: Request password reset email
**Request Body**:
```json
{
  "email": "string"
}
```
**Response**: 200 OK

### 8.3 Subscription Endpoints

#### GET /api/v1/subscriptions
**Description**: List all subscriptions for current user
**Query Parameters**:
- `inactive` (boolean): Include inactive subscriptions
- `category_id` (integer): Filter by category
- `payment_method_id` (integer): Filter by payment method
- `payer_id` (integer): Filter by household member
- `sort` (string): Sort field (name, price, next_payment)
- `order` (string): Sort order (asc, desc)

**Response**: 200 OK
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Netflix",
      "price": 15.99,
      "currency": {
        "id": 1,
        "code": "USD",
        "symbol": "$"
      },
      "cycle": 3,
      "frequency": 1,
      "next_payment": "2025-11-15",
      "auto_renew": true,
      "logo": "netflix_logo.png",
      "category": {
        "id": 1,
        "name": "Entertainment"
      },
      "payment_method": {
        "id": 2,
        "name": "Credit Card"
      },
      "inactive": false
    }
  ],
  "total": 12,
  "page": 1,
  "per_page": 20
}
```

#### GET /api/v1/subscriptions/:id
**Description**: Get subscription details
**Response**: 200 OK

#### POST /api/v1/subscriptions
**Description**: Create new subscription
**Request Body**:
```json
{
  "name": "Spotify",
  "price": 9.99,
  "currency_id": 1,
  "cycle": 3,
  "frequency": 1,
  "next_payment": "2025-11-01",
  "auto_renew": true,
  "url": "https://spotify.com",
  "notes": "Premium family plan",
  "category_id": 1,
  "payment_method_id": 2,
  "payer_user_id": null,
  "notify_days_before": 7
}
```
**Response**: 201 Created

#### PUT /api/v1/subscriptions/:id
**Description**: Update subscription
**Request Body**: Same as POST
**Response**: 200 OK

#### DELETE /api/v1/subscriptions/:id
**Description**: Delete subscription
**Response**: 204 No Content

#### POST /api/v1/subscriptions/:id/mark-inactive
**Description**: Mark subscription as inactive
**Request Body**:
```json
{
  "cancellation_date": "2025-10-20",
  "replacement_subscription_id": null
}
```
**Response**: 200 OK

### 8.4 Currency Endpoints

#### GET /api/v1/currencies
**Description**: List user currencies
**Response**: 200 OK

#### POST /api/v1/currencies
**Description**: Add custom currency
**Request Body**:
```json
{
  "name": "Euro",
  "code": "EUR",
  "symbol": "€",
  "rate": 1.08
}
```
**Response**: 201 Created

#### POST /api/v1/currencies/update-rates
**Description**: Manually trigger exchange rate update
**Response**: 200 OK

### 8.5 Budget Endpoints

#### GET /api/v1/budget
**Description**: Get budget information
**Response**: 200 OK
```json
{
  "status": "success",
  "data": {
    "monthly_budget": 150.00,
    "current_spending": 127.45,
    "utilization": 84.97,
    "projected_yearly": 1529.40,
    "savings_from_inactive": 23.50
  }
}
```

#### PUT /api/v1/budget
**Description**: Update monthly budget
**Request Body**:
```json
{
  "monthly_budget": 200.00
}
```
**Response**: 200 OK

### 8.6 Notification Endpoints

#### GET /api/v1/notifications/settings
**Description**: Get notification settings
**Response**: 200 OK

#### PUT /api/v1/notifications/settings
**Description**: Update notification settings
**Request Body**:
```json
{
  "days_before": 7,
  "email_enabled": true,
  "discord_enabled": false
}
```
**Response**: 200 OK

#### POST /api/v1/notifications/test
**Description**: Send test notification
**Request Body**:
```json
{
  "channel": "email"
}
```
**Response**: 200 OK

### 8.7 OCR Endpoints

#### POST /api/v1/ocr/upload
**Description**: Upload receipt for OCR processing
**Request**: multipart/form-data
- `receipt`: File (image or PDF)
**Response**: 200 OK
```json
{
  "status": "success",
  "data": {
    "extracted_data": {
      "name": "Apple One",
      "price": 14.95,
      "currency": "USD",
      "billing_date": "2025-10-15",
      "cycle": "monthly"
    },
    "confidence": 0.92,
    "receipt_id": 45
  }
}
```

#### POST /api/v1/ocr/create-subscription
**Description**: Create subscription from OCR data
**Request Body**:
```json
{
  "receipt_id": 45,
  "extracted_data": {
    "name": "Apple One",
    "price": 14.95,
    "currency_id": 1,
    "cycle": 3,
    "frequency": 1
  }
}
```
**Response**: 201 Created

### 8.8 AI Insights Endpoints

#### POST /api/v1/insights/analyze
**Description**: Trigger AI analysis
**Response**: 202 Accepted (async processing)

#### GET /api/v1/insights/recommendations
**Description**: Get AI recommendations
**Response**: 200 OK
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "title": "Duplicate Cloud Storage Detected",
      "description": "You have Dropbox, Google Drive, and iCloud. Consider consolidating to save $12/month.",
      "savings": "$12.00",
      "type": "duplicate",
      "related_subscriptions": [5, 8, 12]
    }
  ]
}
```

#### DELETE /api/v1/insights/recommendations/:id
**Description**: Dismiss recommendation
**Response**: 204 No Content

#### GET /api/v1/insights/ml-insights
**Description**: Get ML-powered insights
**Response**: 200 OK

### 8.9 Statistics Endpoints

#### GET /api/v1/stats/overview
**Description**: Dashboard overview stats
**Response**: 200 OK

#### GET /api/v1/stats/spending-trends
**Description**: Spending trends over time
**Query Parameters**:
- `period` (string): month, quarter, year
**Response**: 200 OK

#### GET /api/v1/stats/category-breakdown
**Description**: Cost breakdown by category
**Response**: 200 OK

---

## 9. UI/UX Requirements

### 9.1 Design System

#### Color Palette
- **Primary**: #3B82F6 (Blue 500)
- **Secondary**: #8B5CF6 (Purple 500)
- **Success**: #10B981 (Green 500)
- **Warning**: #F59E0B (Amber 500)
- **Danger**: #EF4444 (Red 500)
- **Background**: #F9FAFB (Gray 50)
- **Surface**: #FFFFFF (White)
- **Text Primary**: #111827 (Gray 900)
- **Text Secondary**: #6B7280 (Gray 500)

#### Typography
- **Font Family**: Inter (sans-serif)
- **Headings**:
  - H1: 2.5rem (40px), font-weight 700
  - H2: 2rem (32px), font-weight 600
  - H3: 1.5rem (24px), font-weight 600
- **Body**: 1rem (16px), font-weight 400
- **Small**: 0.875rem (14px)

#### Spacing Scale
- xs: 0.25rem (4px)
- sm: 0.5rem (8px)
- md: 1rem (16px)
- lg: 1.5rem (24px)
- xl: 2rem (32px)
- 2xl: 3rem (48px)

#### Border Radius
- sm: 0.375rem (6px)
- md: 0.5rem (8px)
- lg: 0.75rem (12px)
- full: 9999px

### 9.2 Page Layouts

#### Dashboard
**Components**:
1. **Header**:
   - App logo
   - Navigation menu
   - User profile dropdown
   - Notifications bell icon

2. **Summary Cards** (4 cards):
   - Total Active Subscriptions
   - Monthly Cost
   - Budget Utilization (progress bar)
   - Upcoming Payments (count)

3. **Main Content**:
   - Upcoming Payments (next 7 days) - card list
   - AI Recommendations - dismissible cards
   - Quick Actions - "Add Subscription" button

4. **Charts** (2-column grid):
   - Spending Trend (line chart)
   - Category Breakdown (donut chart)

#### Subscriptions Page
**Components**:
1. **Toolbar**:
   - Search bar
   - Filter dropdowns (Category, Payment Method, Member, Status)
   - Sort dropdown
   - "Add Subscription" button

2. **Subscription Grid** (responsive cards):
   - Logo
   - Name
   - Price (with currency)
   - Next payment date
   - Quick actions (Edit, Delete, Mark Inactive)

3. **Subscription Form Modal**:
   - Tabbed interface (Basic Info, Billing, Organization)
   - Logo upload/search
   - Form validation
   - Save/Cancel buttons

#### Calendar Page
**Components**:
1. **Month Navigation**:
   - Previous/Next month buttons
   - Month/Year selector

2. **Calendar Grid**:
   - Day cells with payment indicators
   - Hover tooltips with subscription details
   - Multi-subscription days highlighted

3. **Sidebar**:
   - Filters (Category, Member)
   - Legend (color coding)

#### Statistics Page
**Components**:
1. **Time Period Selector**: Month, Quarter, Year
2. **Charts** (responsive grid):
   - Spending Trends (line chart)
   - Category Distribution (pie chart)
   - Payment Method Breakdown (bar chart)
   - Member Comparison (grouped bar chart)
3. **Export Button**: Download CSV report

#### Settings Page
**Components**:
1. **Settings Navigation** (sidebar):
   - Profile
   - Budget
   - Notifications
   - Categories
   - Payment Methods
   - Currencies
   - Household Members
   - Security (2FA)

2. **Settings Content**:
   - Form sections with save buttons
   - Drag-to-reorder lists
   - Toggle switches
   - Test notification buttons

#### OCR Upload Page
**Components**:
1. **Upload Zone**:
   - Drag-and-drop area
   - File browser button
   - Supported formats indicator

2. **Processing Status**:
   - Progress bar
   - OCR provider indicator

3. **Extracted Data Review**:
   - Pre-filled form with extracted data
   - Confidence scores per field
   - Edit capability
   - Confirm/Retry buttons

4. **Receipt Gallery**:
   - Thumbnail grid of uploaded receipts
   - Click to view full image

#### Insights Dashboard
**Components**:
1. **Summary Stats**:
   - Predicted next month cost
   - Anomalies detected
   - Optimization opportunities

2. **Insights Feed**:
   - Card-based layout
   - Color-coded by severity (info, warning, critical)
   - Dismiss/Action buttons

3. **Visualizations**:
   - Spending heatmap (calendar-based)
   - Forecast vs actual chart
   - Anomaly timeline

### 9.3 Responsive Design
- **Desktop** (1200px+): Full layout with sidebar navigation
- **Tablet** (768px - 1199px): Collapsible sidebar, 2-column grids
- **Mobile** (<768px): Bottom navigation, single-column layout, stacked cards

### 9.4 Accessibility
- WCAG 2.1 AA compliance
- Keyboard navigation support
- ARIA labels for screen readers
- Color contrast ratios: 4.5:1 minimum
- Focus indicators on interactive elements
- Error messages associated with form fields

### 9.5 Interactions & Animations
- **Hover**: Scale 1.02, shadow elevation
- **Click**: Scale 0.98, ripple effect
- **Page Transitions**: Fade in (200ms)
- **Modal Appearance**: Slide up (300ms) with backdrop fade
- **Toast Notifications**: Slide in from top-right
- **Loading States**: Skeleton screens, spinner overlays

---

## 10. Security & Privacy

### 10.1 Authentication Security
- **Password Requirements**:
  - Minimum 8 characters
  - At least 1 uppercase, 1 lowercase, 1 number
  - No common passwords (dictionary check)
  - Bcrypt hashing (cost factor 12)

- **Session Security**:
  - HttpOnly cookies
  - SameSite=Strict
  - Secure flag (HTTPS only)
  - 30-day expiration
  - CSRF tokens on state-changing requests

- **2FA (TOTP)**:
  - SHA-1 based TOTP (RFC 6238)
  - 30-second time window
  - 6-digit codes
  - Backup codes (10 codes, one-time use)

### 10.2 Data Encryption
- **At Rest**:
  - SQLite encryption (SQLCipher extension optional)
  - Sensitive fields encrypted (SMTP passwords, API keys)
  - AES-256 encryption

- **In Transit**:
  - HTTPS enforced (TLS 1.2+)
  - HSTS headers
  - Certificate pinning (optional)

### 10.3 Input Validation
- **Server-side Validation**:
  - Type checking
  - Length limits
  - Regex patterns
  - SQL injection prevention (parameterized queries)
  - XSS prevention (HTML escaping)

- **Client-side Validation**:
  - Real-time feedback
  - Format hints
  - Duplicate server-side checks

### 10.4 Authorization
- **RBAC**:
  - Admin role: User management, system settings
  - User role: Own subscriptions, household members

- **Data Isolation**:
  - All queries filtered by user_id
  - No cross-user data access
  - Cascade deletion on user removal

### 10.5 Privacy
- **Data Minimization**:
  - Only collect necessary data
  - Optional fields for URLs, notes
  - Anonymous AI analysis (no PII sent)

- **Data Retention**:
  - User-controlled data deletion
  - Inactive subscription archival
  - Receipt retention (user choice)

- **Third-Party Services**:
  - Fixer.io: API key optional (fallback manual rates)
  - AI providers: User choice (local Ollama for privacy)
  - OCR: Local Tesseract default (Google Vision opt-in)

### 10.6 Audit Logging
- Log sensitive actions:
  - User login/logout
  - Password changes
  - Subscription creation/deletion
  - Budget modifications
  - Notification sent
- Log retention: 90 days
- Admin access to logs

---

## 11. Integration Requirements

### 11.1 Fixer.io API
- **Purpose**: Currency exchange rates
- **API Key**: User-provided (optional)
- **Endpoint**: `https://api.fixer.io/latest`
- **Frequency**: Daily update (2:00 AM)
- **Error Handling**: Fallback to last known rates
- **Rate Limiting**: 100 requests/month (free tier)

### 11.2 AI Providers

#### OpenAI ChatGPT
- **Model**: GPT-4 or GPT-3.5-turbo
- **API Key**: User-provided
- **Use Case**: Subscription optimization recommendations
- **Request Format**: JSON with subscription list
- **Response**: Structured recommendations
- **Cost**: ~$0.01 per analysis

#### Google Gemini
- **Model**: Gemini Pro
- **API Key**: User-provided
- **Use Case**: Alternative to ChatGPT
- **Cost**: Free tier available

#### Ollama (Local)
- **Models**: Llama 2, Mistral, others
- **Deployment**: User self-hosts Ollama server
- **Use Case**: Privacy-focused AI (no external calls)
- **Cost**: Free (hardware only)

### 11.3 OCR Providers

#### Tesseract OCR
- **Deployment**: Bundled with application
- **Languages**: 100+ supported
- **Accuracy**: 80-90% (varies by image quality)
- **Cost**: Free (open-source)

#### Google Vision API
- **API Key**: User-provided (optional)
- **Accuracy**: 95%+ (handwriting support)
- **Cost**: $1.50 per 1000 images
- **Rate Limiting**: 1800 requests/minute

### 11.4 Notification Channels

#### Email (SMTP)
- **Configuration**: User-provided server
- **Common Providers**: Gmail, SendGrid, Mailgun
- **Authentication**: Username/password or OAuth

#### Discord
- **Integration**: Webhook URL
- **Setup**: Create webhook in Discord channel settings
- **Format**: Rich embeds with colors

#### Telegram
- **Integration**: Bot API
- **Setup**: Create bot via BotFather, get token
- **Format**: Markdown formatted messages

#### Pushover
- **Integration**: User key + API token
- **Setup**: Register app on Pushover
- **Priority**: Support for emergency, high, normal, low

#### Others (PushPlus, Mattermost, Ntfy, Gotify)
- Similar webhook/token-based integrations
- Provider-specific documentation

---

## 12. Success Metrics

### 12.1 Product Metrics

**Adoption**:
- Number of active users
- Number of subscriptions tracked
- Average subscriptions per user: Target 8-12

**Engagement**:
- Daily active users (DAU): Target 60% of total users
- Weekly logins: Target 80%
- Feature usage: OCR adoption 40%, AI insights viewed 50%

**Financial Impact**:
- Average monthly savings per user: Target $25
- Subscriptions canceled: Target 15% of total
- Budget adherence rate: Target 70% users within budget

**Notification**:
- Notifications sent: Track volume per channel
- Notification success rate: Target 98%
- Missed payment reduction: Target 90% reduction

### 12.2 Technical Metrics

**Performance**:
- API response time: <200ms (p95)
- Dashboard load time: <1s
- OCR processing time: <5s per receipt
- Database query time: <50ms (p95)

**Reliability**:
- Uptime: 99.5%
- Error rate: <0.1%
- Successful notification delivery: 98%
- Data backup success: 100%

**Security**:
- Zero data breaches
- Zero unauthorized access incidents
- Password reset success rate: 95%
- 2FA adoption: Target 30% of users

### 12.3 User Satisfaction

**Surveys**:
- Net Promoter Score (NPS): Target 40+
- User satisfaction: Target 4.5/5
- Feature request volume: Track top requests

**Support**:
- Issue resolution time: <24 hours
- Self-service documentation usage: 70%
- Support ticket volume: Track trends

---

## 13. Future Roadmap

### 13.1 Phase 2 Features (v2.0)

**Bank Integration**:
- Plaid API integration for automatic subscription detection
- Transaction categorization
- Real-time spending alerts

**Usage Tracking**:
- Browser extension for usage tracking
- Mobile app usage integration
- "Unused subscription" detection based on activity

**Enhanced ML**:
- Subscription usage prediction
- Cancellation risk scoring
- Personalized renewal reminders

**Mobile App**:
- Native iOS/Android apps
- Push notifications
- Mobile receipt capture
- Widget support

### 13.2 Phase 3 Features (v3.0)

**Team Plans**:
- Business subscription management
- Team budgets and approval workflows
- Department-level tracking

**Advanced Analytics**:
- ROI tracking per subscription
- Benchmark against industry averages
- Subscription lifecycle analysis

**Marketplace**:
- Subscription deal aggregator
- Referral links with cashback
- Community-driven reviews

**API Platform**:
- Public API for third-party integrations
- Developer documentation
- API rate limiting and keys

---

## Appendix

### A. Glossary
- **Billing Cycle**: Frequency of subscription charges (daily, weekly, monthly, yearly)
- **OCR**: Optical Character Recognition - converting images to text
- **TOTP**: Time-based One-Time Password - 2FA method
- **RBAC**: Role-Based Access Control
- **Anomaly Detection**: ML technique to identify unusual patterns

### B. References
- Wallos GitHub: https://github.com/ellite/Wallos/
- Fixer.io API Docs: https://fixer.io/documentation
- Tesseract OCR: https://github.com/tesseract-ocr/tesseract
- Google Vision API: https://cloud.google.com/vision/docs

### C. Change Log
- v1.0 (2025-10-19): Initial PRD draft

---

**Document Status**: Draft
**Next Review Date**: 2025-11-01
**Approval Required**: Product Team, Engineering Lead