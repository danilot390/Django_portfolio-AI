# PERSONAL AI PORTFOLIO WEBSITE 

## 1. Overview
This project is a modular, production-ready personal portfolio website built with Django. It is designed to showcase professional experience, education, projects, skills, and achievements through a clean and maintainable architecture.

The application is fully containerized using Docker and orchestrated with Docker Compose. It includes dynamic content management, automated database seeding, static asset handling, and CV generation with PDF export capabilities.

the project is build with scalability and extensibility and extensibility in mind, enabling future integration of AI-powered features such as intelligent assistants, project recommendation systems, data visualization tools, and machine learning model deployment.

---

## 2. Features
* Django-based portfolio application.
* Responsive UI built with Tailwind CSS.
* Fully containerized environment using Docker & Docker Compose.
* Production-ready deployment with Gunicorn.
* Automated database migrations and initial data seeding.
* Static file management with WhiteNoise.
* Dynamic CV generation with HTML-to-PDF export.
* Downloadable CV endpoint with custom filenames.
* Contact form with automated email notifications.
* Modular application architecture (`core`, `projects`, `contact`, and `cv` apps).
* Django Admin panel for content management.
* Evironment-based configuration using `.env` file.

---

## 3. Tech Stack

* **Backend:** Django, Django REST Framework.
* **Database:** PostgreSQL (default), easily adaptable to other Database Management System (DBMS).
* **Frontend:** Django Templates, and Tailwind CSS.
* **Environment:** Python, Virtual environments (`venv`), `python-decouple`.
* **Conteinerizement:** Docker, and Docker Compose.
* **Deployment:** Gunicorn, WhiteNoise, and Nginx.

---

## 4. Project Structure
```text
Django_portfolio-AI/
├── apps/
│   ├── core/
│   ├── contact/
│   ├── cv/
│   └── projects/
├── config/
├── pdf-service/
├── requirements/
│   ├── base.txt 
│   ├── dev.txt 
│   └── prod.txt
├── static/
├── templates/
├── .env
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── package-lock.json
├── package.json
├── postcss.config.js
├── tailwind.config.js
└── manage.py
```

---
 
## 5. Installation

### Clone the repository
```bash
git clone https://github.com/danilot390/Django_portfolio-AI.git
cd Django_portfolio-AI
```

### Environment variables
Create a `.env` file in the project root directory.

> **Note:** Adjust the variables according to your evironment and review `.env.example` for additional details.

### Build and run the containers
```Bash
docker compose up --build
```
This command will:

* Build Django application image.
* Start the PostgreSQL database service. 
* Apply database migrations. 
* Collect static files.
* Launch the Gunicorn application server.
* Start the Pdf generation services.

>**Note:** By default, the application will be avaible at `http://127.0.0.1:8000`.

#### Seed the Database
Populate the database using the YAML seed files located in `apps/projects/management/seeds/`.

Run:

``` bash
docker exec -it portfolio_web sh 
python manage.py seed_portfolio
```

>**Note:** You can customize the seed data by following the existing file structure and conventions.

---

### Development Mode (Without Docker)

#### Create a Virtual Environment (Optional)
```bash
python -m venv .venv
```

Activate the environment:
**macOS/Linux**
```bash
source .venv/bin/activate
```
**Windows**
```cmd 
.venv\Scripts\activate
```

#### Install Python dependencies

Base requirements:
```bash 
pip install -r requirements/base.txt
```

Development requirements:
```bash 
pip install -r requirements/dev.txt
```

Production requirements:
```bash 
pip install -r requirements/prod.txt
```

#### Install Frontend dependencies
```bash
npm install
```

#### Database Setup
1. Create the databe manually using your preferred database  management tool.
2. Install the appropiate database adapter.

**PostgreSQL (Default)**
```bash
pip install psycopg2-binary
```

**MySQL**
```bash
pip install mysqlclient
```

For other database engines, refer to the official Django database documentation.

> **Note:** Always verify version compatibility between Python version, Django version and Database driver server.

#### Apply Migrations and Seed Data
```bash
python manage.py migrate
python manage.py seed_portfolio
```

#### Run Development server
```bash
python manage.py runserver
```
Access the application at: `http://127.0.0.1:8000/`

#### Tailwind Development Mode
Run the whatcher in a separate terminal:

```bash 
npm run dev
```

#### Production Build
Generate optimized CSS assets:

```bash
npm run build
```

### Management Commands
Seed the database `python manage.py seed_portfolio`.

This command populates:

* Personal information.
* Profiles.
* Tags and technologies.
* Skills.
* Education records.
* Projects.
* Professional experience.

---

## 6. Production Notes
* Set `DEBUG=False`.
* Use strong and secure `SECRET_KEY`.
* Configure `ALLOWED_HOSTS` correctly.
* Use Nginx as a reverse proxy in front of Gunicorn.
* Configure persistent PostgreSQL volumes for data retention.

---

## 7. Roadmap 
Planned enhancements include:

* AI-powered chatbot assitant.
* Project recommendation engine.
* Machine Learning model deployment.
* Interactive analytics dashboards.
* Exppanded REST API.
* CI/CD pipeline integration.
* Multi-theme CV support.

---

## 8. License
This project is licensed under the MIT License. See the LICENSE file for details.