🧬 AI Health Risk Prediction System

Python | Flask | React.js | MySQL | Machine Learning

An AI-powered full-stack web application that analyzes patient biometric and lifestyle data to predict health risks including Diabetes and Cardiovascular Disease using a trained Random Forest Machine Learning model — with real-time risk scoring, personalized wellness recommendations, and a premium glassmorphic dashboard.

🗺️ System Architecture

User → React.js Frontend (Vite) ↓ JWT Auth (Axios) Flask REST API Backend ↓ MySQL Database ←→ ML Engine (Random Forest) ↓ Risk Score + Recommendations

---
## ✨ Key Features & Capabilities
### 🤖 1. AI-Powered Risk Prediction Engine
- **Multi-Disease Prediction:** Simultaneously assesses risk for Diabetes and Heart Disease using a trained Random Forest classifier.
- **Clinical Biomarker Analysis:** Processes blood glucose, HbA1c, blood pressure, cholesterol, and BMI for comprehensive risk profiling.
- **Real-Time Health Scoring:** Dynamically computes a 0–100 health score based on weighted biometric inputs.
- **Risk Classification:** Categorizes patients as Low, Moderate, or High risk with confidence percentages.
### 📋 2. Multi-Step Health Assessment Form
- **Structured Input Sections:** Organized into Personal & Body Metrics, Clinical Biomarkers, and Lifestyle & Medical History.
- **Smart Validation:** Client-side and server-side validation ensures accurate data entry before prediction.
- **Lifestyle Profiling:** Captures smoking history, exercise frequency, alcohol consumption, and family medical history.
- **Cholesterol Mapping:** Intelligently maps descriptive cholesterol labels to numeric clinical ranges for ML processing.
### 📊 3. Premium Glassmorphic Dashboard
- **Health Score Gauge:** Animated SVG gauge displaying live health score with color-coded risk indicators.
- **Prediction History Tracking:** Complete log of past assessments with timestamps and risk trend visualization.
- **Wellness Recommendations:** AI-generated personalized health tips based on identified risk factors.
- **Profile Management:** Editable user profiles with biometric history and assessment summaries.
### 🔐 4. Secure Authentication System
- **JWT-Based Auth:** Stateless JSON Web Token authentication for secure API access.
- **Protected Routes:** React Router guards prevent unauthorized access to dashboard pages.
- **Session Persistence:** Tokens stored with auto-refresh logic for seamless user sessions.
---
## 🛠️ Tech Stack & Dependencies
| Layer | Technology |
|---|---|
| **Frontend** | React.js (Vite), HTML5, CSS3, JavaScript |
| **Backend** | Python 3.x, Flask REST API |
| **Database** | MySQL, SQLAlchemy ORM |
| **ML Engine** | Scikit-learn (Random Forest Classifier) |
| **Auth** | JWT (Flask-JWT-Extended) |
| **Styling** | Glassmorphism UI, Inter + Space Grotesk fonts |
| **HTTP Client** | Axios |
---
## 📦 Installation & Setup
### 1. Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Node.js 18+ and npm/pnpm
- MySQL Server
---
### 2. Quickstart Guide
**Clone the Repository:**
```bash
git clone https://github.com/yourusername/AI-Health-Risk-Prediction-System.git
cd AI-Health-Risk-Prediction-System

Backend Setup:

bash
cd backend
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

Environment Variables: Create a .env file inside /backend:

env
# Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=health_risk_db
# Auth
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
# App
FLASK_ENV=development

Initialize Database:

bash
python init_db.py

Start Backend Server:

bash
python app.py

Frontend Setup:

bash
cd frontend
npm install
npm run dev

Open http://localhost:5173
 in your browser.

📁 Project Structure
AI-Health-Risk-Prediction-System/
│
├── backend/
│   ├── models/              # SQLAlchemy DB models (User, Assessment, Prediction)
│   ├── routes/              # Flask API route blueprints
│   │   ├── auth.py          # Login, Register, JWT endpoints
│   │   ├── assessment.py    # Health assessment submission
│   │   ├── predict.py       # ML prediction engine
│   │   └── dashboard.py     # Dashboard data endpoints
│   ├── services/            # Business logic layer
│   │   ├── health_service.py    # BMI & health score calculator
│   │   └── recommendation_service.py  # AI recommendation engine
│   ├── utils/               # Utility helpers (calculators, validators)
│   ├── ml_model/            # Trained Random Forest model (.pkl)
│   ├── app.py               # Main Flask application entry point
│   ├── init_db.py           # Database initialization script
│   └── requirements.txt     # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── api/             # Axios API service layer
│   │   ├── components/      # Reusable UI components (Sidebar, Cards)
│   │   ├── context/         # React Context (Auth, Toast)
│   │   ├── layouts/         # DashboardLayout wrapper
│   │   ├── pages/           # Route-level pages
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── HealthAssessment.jsx
│   │   │   ├── Prediction.jsx
│   │   │   ├── History.jsx
│   │   │   ├── Wellness.jsx
│   │   │   ├── Recommendation.jsx
│   │   │   └── Profile.jsx
│   │   ├── App.jsx          # Router configuration
│   │   ├── main.jsx         # React entry point
│   │   └── index.css        # Global premium theme & glassmorphism styles
│   ├── index.html
│   └── vite.config.js
│
└── README.md
🖥️ Screenshots
Dashboard	Health Assessment	Risk Prediction
Health Score Gauge	Multi-step Form	AI Risk Report
🛡️ License & Contributions
Contributions: Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
License: Distributed under the MIT License. See LICENSE for details.

⚕️ Disclaimer: This system is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---
Copy the entire block above into your `README.md` file on GitHub! 🎯
