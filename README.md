# PERSONAL AI PORTFOLIO WEBSITE 

## Overview
This project is a modular, Django-based personal website designed to reflect professional background, and showcase AI, Machine Learning and Analityics projects. 
The architecture is built to scale into AI-powered features including chatbots, data tools, and ML model deployment.

## Tech Stack
- Backend: Django, Django REST Framework
- Database: PostgreSQL
- Frontend: Django Templates + Tailwind CSS
- Environment: Python(venv), python-decouple
- Deployment (planned): Gunicorn, WhiteNoise

## Setup & Installation

### Create virtual environment (Optional)
```py
python -m venv .venv
```
Activate it:
* macOS/Linux
```bash
source .venv/bin/activate
```
* Windows
```bash 
.venv\Scripts\activate
```

### Install dependencies
```bash 
pip install -r requirements/base.txt
```

### Install development dependencies (Optional)
Install *in the case you are contributing or developing locally*.
```bash 
pip install -r requirements/dev.txt
```

### Install production dependencies (Deployment only)
These are required *only when deploying the application to production*.
```bash 
pip install -r requirements/prod.txt
```

### Environment variables
Create a .env file inthe root directory:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:passwrod@localhost:5432/db_name
```
### Apply migrations 
```bash
python manage.py migrate
```
### Run development server
```bash
python manage.py runserver
```
Access the app at: `http://127.0.0.1:8000/`
