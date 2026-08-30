# 🏥 RuralCare — Healthcare Access Platform

A modern, scalable healthcare platform designed to improve access to healthcare information and services in rural communities. The application combines a **React.js frontend**, **FastAPI backend**, and **MySQL database** to provide a simple and efficient healthcare management experience.

## ✨ Features

* 🏥 Healthcare centre information
* 📋 Health records management
* 📚 Health information access
* 🔎 Search and view healthcare details
* 🌐 REST API using FastAPI
* 💾 MySQL database integration
* ⚡ Fast and lightweight backend
* 📱 Responsive modern UI
* 📶 Designed with low-bandwidth environments in mind
* 🔄 Frontend connected directly to backend APIs

## 🛠️ Tech Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* Vite

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy

### Database

* MySQL

### Development Tools

* VS Code
* Git
* GitHub
* Postman

## 📂 Project Structure

```text
healthcare/
│
├── rural-area/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.jsx
│   │   │   ├── HealthcareAccess.jsx
│   │   │   ├── HealthRecords.jsx
│   │   │   └── HealthInformation.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── index.html
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── venv/
│
└── README.md
```

## 🗄️ Database

The project uses MySQL to store healthcare-related information.

### Main Tables

#### `healthcare_centres`

Stores information about healthcare centres.

| Column    | Type    | Description               |
| --------- | ------- | ------------------------- |
| `id`      | INT     | Primary key               |
| `name`    | VARCHAR | Healthcare centre name    |
| `address` | TEXT    | Centre address            |
| `phone`   | VARCHAR | Contact number            |
| `type`    | VARCHAR | Type of healthcare centre |

#### `health_records`

Stores patient health record information.

The database layer is handled using **SQLAlchemy ORM**, allowing the FastAPI backend to communicate with MySQL efficiently.

## 🔌 API

The backend provides RESTful API endpoints through FastAPI.

Example endpoints:

```text
GET /health
GET /healthcare-centres
GET /health-records
POST /healthcare-centres
POST /health-records
```

FastAPI also automatically provides interactive API documentation.

After starting the backend, open:

```text
http://127.0.0.1:8000/docs
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd RuralCare
```

### 2. Setup Backend

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
python -m uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 3. Setup MySQL

Create the database:

```sql
CREATE DATABASE healthcare;
```

Make sure the MySQL credentials in your backend configuration match your local MySQL installation.

### 4. Setup Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

The frontend will be available at the URL shown by Vite, usually:

```text
http://localhost:5173
```

## 🔗 Application Architecture

```text
             👤 User
                │
                ▼
       ┌─────────────────┐
       │   React.js UI   │
       │    Frontend     │
       └────────┬────────┘
                │
             REST API
                │
                ▼
       ┌─────────────────┐
       │     FastAPI     │
       │     Backend     │
       └────────┬────────┘
                │
           SQLAlchemy
                │
                ▼
       ┌─────────────────┐
       │      MySQL      │
       │    Database     │
       └─────────────────┘
```

## 🎯 Problem Statement

Healthcare access in rural areas can be affected by limited infrastructure, lack of accessible information, low digital literacy, and connectivity challenges.

RuralCare aims to provide a **simple, modular, and lightweight digital platform** that can make healthcare-related information easier to access while supporting environments with limited connectivity.

## 🌱 Future Improvements

* 📶 Full offline-first functionality
* 🌍 Regional language support
* 🗺️ Healthcare centre location mapping
* 👨‍⚕️ Doctor availability
* 📅 Appointment management
* 🔔 Health reminders
* 🤖 AI-powered healthcare assistance
* 🔐 Authentication and role-based access
* ☁️ Cloud deployment
* 📊 Healthcare analytics dashboard

## 👩‍💻 Author

**Yashvanthika G**

AI & Data Science Student

## 📄 License

This project is developed for educational and project purposes.
