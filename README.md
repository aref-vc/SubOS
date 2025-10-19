# SubOS - Personal Subscription Manager

> Self-hosted, privacy-first subscription management platform with AI-powered insights and OCR receipt processing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)

## Overview

SubOS helps you track recurring subscriptions, manage budgets, and optimize spending through intelligent recommendations. Built with privacy in mind, all your data stays on your machine.

### Key Features

- 📊 **Unlimited Subscription Tracking** - Track any recurring expense with flexible billing cycles
- 💱 **Multi-Currency Support** - Real-time exchange rates with 150+ currencies
- 💰 **Budget Management** - Set budgets and track spending against goals
- 🔔 **9 Notification Channels** - Email, Discord, Telegram, Pushover, and more
- 🤖 **AI-Powered Recommendations** - Cost optimization suggestions via ChatGPT, Gemini, or local Ollama
- 📸 **OCR Receipt Processing** - Scan receipts to auto-populate subscription details
- 📈 **ML-Powered Insights** - Anomaly detection, spending predictions, and pattern analysis
- 🏠 **Household Management** - Track subscriptions across family members
- 🔒 **Security First** - TOTP 2FA, bcrypt password hashing, session management
- 🎨 **Clean UI** - Minimal design with JetBrains Mono and Integrations UI system

## Tech Stack

- **Backend**: Python 3.11+, Flask/FastAPI, SQLAlchemy, SQLite
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **ML/AI**: scikit-learn, OpenAI API, Google Gemini, Ollama
- **OCR**: Tesseract, Google Vision API
- **Notifications**: APScheduler with 9 channel integrations

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- SQLite 3

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/aref-vc/SubOS.git
cd SubOS
```

2. **Set up the backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Run database migrations**
```bash
alembic upgrade head
```

5. **Set up the frontend**
```bash
cd ../frontend
npm install
```

6. **Start the application**

**Option 1: Manual start**
```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python run.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

**Option 2: Quick launch script**
```bash
chmod +x scripts/start.sh
./scripts/start.sh
```

7. **Access the application**
- Frontend: http://localhost:5173
- Backend API: http://localhost:3038
- API Docs: http://localhost:3038/api/docs

## Documentation

- **[PRD.md](PRD.md)** - Complete product requirements and specifications
- **[IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)** - 18-week development roadmap with code examples

## Project Structure

```
SubOS/
├── backend/              # Flask/FastAPI application
│   ├── app/
│   │   ├── models/      # SQLAlchemy models
│   │   ├── api/         # REST API endpoints
│   │   ├── services/    # Business logic
│   │   ├── tasks/       # Scheduled jobs
│   │   └── utils/       # Utilities
│   ├── tests/           # Backend tests
│   └── requirements.txt
├── frontend/            # React application
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API client
│   │   └── styles/      # CSS files
│   └── package.json
├── scripts/             # Utility scripts
├── .env.example         # Environment template
├── .gitignore
└── README.md
```

## Configuration

Create a `.env` file in the root directory:

```env
# Application
DEBUG=True
SECRET_KEY=your-secret-key-here
PORT=3038

# Database
DATABASE_URL=sqlite:///subos.db

# Optional API Keys
FIXER_API_KEY=your-fixer-api-key
OPENAI_API_KEY=your-openai-key
GOOGLE_VISION_API_KEY=your-google-vision-key
```

## Features in Detail

### Subscription Management
- Flexible billing cycles (daily, weekly, monthly, yearly)
- Custom frequency (every N periods)
- Auto-renewal tracking
- Logo management (upload or web search)
- Category organization
- Payment method tracking
- Inactive subscription archival

### Notifications
Supported channels:
- Email (SMTP)
- Discord (Webhooks)
- Telegram (Bot API)
- Pushover
- PushPlus
- Mattermost
- Ntfy
- Gotify
- Generic Webhooks

### AI & ML Features
- Cost optimization recommendations
- Duplicate subscription detection
- Alternative service suggestions
- Anomaly detection (Isolation Forest)
- Spending predictions (ARIMA)
- Subscription clustering (K-means)

### OCR Processing
- Tesseract OCR (local, privacy-focused)
- Google Vision API (cloud, higher accuracy)
- Automatic field extraction
- Receipt archive with full-text search

## Development

### Running Tests

**Backend**
```bash
cd backend
source venv/bin/activate
pytest
```

**Frontend**
```bash
cd frontend
npm test
```

### Code Style

- Python: Follow PEP 8
- TypeScript/React: ESLint + Prettier
- Commits: Conventional Commits format

## Roadmap

See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for the complete 18-week development roadmap.

**Current Phase**: Foundation (Week 1-2)
- Database schema implementation
- Core models
- Basic API structure

**Upcoming**:
- Phase 2: Core Features (Subscriptions, Auth, Currencies)
- Phase 3: Notifications (9 channels)
- Phase 4: Advanced Features (AI, Household, Analytics)
- Phase 5: ML Insights & OCR
- Phase 6: Frontend Development
- Phase 7: Testing & Deployment

## Contributing

Contributions are welcome! Please read the implementation plan and follow the code style guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Inspiration

This project is inspired by [Wallos](https://github.com/ellite/Wallos/), an excellent self-hosted subscription tracker. SubOS extends the concept with ML-powered insights, OCR processing, and a modern tech stack.

## Support

For questions or issues:
- Open an issue on GitHub
- Check the [PRD.md](PRD.md) for detailed feature specifications
- Review [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for technical details

## Acknowledgments

- Design System: Integrations UI (clean minimal design)
- Font: JetBrains Mono
- Icons: Lucide React
- Inspired by: Wallos project

---

**Built with ❤️ for privacy-conscious subscription management**
