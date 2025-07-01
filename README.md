# TravelTrip - AI-Powered Travel E-commerce Platform 🌍✈️

An intelligent travel booking platform that combines modern web technologies with AI-powered recommendations to provide personalized travel experiences.

## 🚀 Features

- **AI-Powered Chatbot**: Intelligent travel assistant with RAG (Retrieval-Augmented Generation) system
- **Dynamic Product Recommendations**: Personalized travel suggestions based on user preferences
- **Real-time Booking System**: Seamless reservation management for hotels, flights, and activities

## 🏗️ Architecture

![TravelTrip Architecture](docs/architecture-diagram.svg)

### Tech Stack

**Frontend:**
- React.js 18+ with modern hooks
- CSS3 with responsive design
- Interactive ChatWidget for AI assistance

**Backend:**
- Django 4.2+ with Django REST Framework
- Python 3.9+
- Modular app architecture (accounts, bookings, cart, trips, chatbot)

**Database:**
- PostgreSQL 13+ for reliable data storage
- Optimized queries for travel data

**AI/ML:**
- LLM RAG System for intelligent responses
- Vector search for semantic understanding
- Product recommendation engine

**DevOps:**
- Docker & Docker Compose for containerization
- Environment-based configuration

## 📁 Project Structure

```
TRAVELTRIP_PROJECT/
├── frontend/                    # React frontend application
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── ChatWidget.js       # AI chatbot interface
│   │   └── ...
│   ├── package.json            # Node.js dependencies
│   └── public/
├── backend/                     # Django backend
│   ├── TRAVELTRIP_PROJECT/     # Main project settings
│   ├── accounts/               # User management
│   ├── bookings/               # Reservation system
│   ├── cart/                   # Shopping cart functionality
│   ├── chatbot/                # AI chatbot backend
│   ├── trips/                  # Travel products management
│   ├── media/                  # User uploaded files
│   ├── static/                 # Static assets
│   └── requirements.txt        # Python dependencies
├── ai_system/                  # AI/LLM RAG components
│   ├── llm_service.py          # LLM integration
│   ├── vector_search.py        # Semantic search
│   └── recommendation.py       # Product recommendations
├── docker-compose.yml          # Container orchestration
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for local development)
- Node.js 16+ (for frontend development)
- PostgreSQL 13+ (if running without Docker)

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/traveltrip.git
   cd traveltrip
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

### Local Development Setup

#### Backend Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Django server**
   ```bash
   python manage.py runserver
   ```

#### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server**
   ```bash
   npm start
   ```

## 📚 API Documentation

### Main Endpoints

- **Authentication**: `/api/auth/`
- **User Management**: `/api/accounts/`
- **Trip Products**: `/api/trips/`
- **Bookings**: `/api/bookings/`
- **Shopping Cart**: `/api/cart/`
- **AI Chatbot**: `/api/chatbot/`

### Example API Usage

```javascript
// Get travel recommendations
fetch('/api/chatbot/recommend/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your-token'
  },
  body: JSON.stringify({
    message: "I want to visit Japan in spring",
    preferences: ["culture", "nature", "food"]
  })
})
```

## 🚀 Deployment

### Production Deployment

1. **Update environment variables for production**
2. **Build production Docker image**
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ``

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





⭐ **Star this repository if you find it helpful!**
