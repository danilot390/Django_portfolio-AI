All notabel changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/)

---
## [1.0.1] - 2026-06-27
([commit ]())

### Added
- Created railway.json for platform configuration.

### Changed
- Adjusted config/settings.py for environment variables.

### Fixed
- Update Django Dockerfile for production build.

---
## [1.0.0] - 2026-06-24
([commit f7707a9](https://github.com/danilot390/Django_portfolio-AI/commit/f7707a9496c4c9f618105eef0b0743089d923736))

### Added
- Implemented Docker Compose configuration and containerized deployment setup.
- Created Docker support for the Django application.
- Added Docker Compose configuration for multi-service deployment.
- Integrated Django container entrypoint.
- Added `.dockerignore`.
- Added environment variable template (`.env.example`).
- Implemented CV application for managing summary presentation.
- Added printable CV templates with reusable sections including summary, skills, projects, professional experience, education, languages, interests, and highlights.
- Integrated CV-specific viewsm routing, selectors and admin integration.
- Introduced PDF client abstraction for comunication with the PDF generation.
- Added dedicated PDF generation service for CV exports.
- Integrated standalon Node.js PDF generation service.
- Implemented PlayWright for server-side PDF rendering.
- Added REST endpoint for PDF generation.
- Integrated Docker image for the PDF service.
- Created structured seed data for professional experiences including Freelancer, Web developer for Government Autonomous Department of Potosi, and Universidad Autonoma Tomas Frias.
- Created experience seed datasets.
- Generated Core and Projects database migrations.
- Generated new Core migration supporting CV-related profile changes.
- Generated new Project migration for updated experience and project models.

### Changed 
- Extended portfolio domain models.
- Improved About page presentation.
- Updated profile configuration for CV support.
- Updated DJango admin configuration.
- Refactored project and experience models.
- Improved portfolio seeding pipeline.
- Expanded and updated taxonomy, technologies, tags adn people datasets.
- Updated seed portfolio management scripts.
- Updated Django settings to support containerized deployment.
- Updated root URL configuration.
- Expanded and complete README with deployment and production.
- Updated shared base template.
- Improved navigation for the new CV section.

### Removed
- Removed deprecated experience image handling from project-related models.

### Fixed
- Fixed Python dependency definitions for develpment and production.

---
## [0.4.0] - 2026-05-28
([commit dd9cce4](https://github.com/danilot390/Django_portfolio-AI/commit/dd9cce47d63f56bcb147b96076925309323e8f1c))

### Added
- Implemented contact application.
- Created contact form handling using Django forms.
- Created contact service layer for business logic separation.
- Implemented contact page template and routing.
- Generated initial database migration for contact message models.
- Created experience management system.
- Created experience listing and detail page templates.
- Implemented experience presentation views.
- Created reusable person component.
- Generated project migration updates for experience management.
- Added initial migrations for Core and Project applications.
- Added missing `__init__.py` files.

### Changed
- Refactored contact app configuration and admin integration.
- Updated contact message model structure and metadata.
- Extended contact view logic for form-processing workflows.
- Updated Core application.
- Aggregated homepage content integration to include experience and contact navigation.
- Included URL routing for experience-related pages.
- Extended core admin configuration for content management.
- Updated project admin configuration.
- Refined project model options and taxonomy relationships.
- Extended global base template navigation and layout.
- Extended Tailwind configuration for new templates and UI components.
- Updated Django settings and root URL to include contact app.
- Updated Python dependencies to include `pyyaml` & `resend` libraries.

### Fixed
- Fixed `.gitignore` configuration to track `__init__.py` files.

---
## [0.3.0] - 2026-05-19
([commit 7159d37](https://github.com/danilot390/Django_portfolio-AI/commit/7159d375f836d6ae72fd7f34eb9864f4387cff01))

### Added
- Add About section display personal information.
- Add dynamic template for About page.
- Add doomain models for the About section.
- Add database migrations for portfolio model updates.
- Add modular portfolio seeding architecture using structured YAML data.
- Add `seed_portfolio` management command with reusable seed loader modules.

### Changed 
- Update admin configuration for portfolio-related models.
- Refactor core models for improve extensiblity.
- Restrutured homepage content layout.
- Update routing and view logic for dynamic pages.
- Refactor reusable person link components.
- Improve project listing template structure
- Update shared base template layout and navigation menu.
- Update Python package requierments.

### Removed
- Remove deprecated `seed_projects` command and its `helper.py` file.

---

## [0.2.0] - 2026-05-10
([commit 8d949dd](https://github.com/danilot390/Django_portfolio-AI/commit/8d949dd07a002e6612e4541f7404b66264404aa5))

### Added
- Frontend asset processing workflow.
- Initial `core` and `projects` app structure.
- Templates for core and projects pages.
- Django migrations for core and projects apps.
- Project-specific URL routing.
- Management utilities for projects apps.
- Tailwind CSS frontend pipeline with PostCSS configuration.
- Static asset structure
- Global templates directory

### Changed 
- Updated Django settings and root URL configuration.
- Updated app configurations for `core` and `projects`.
- Expanded models, views, and admin registration for both apps.
- Improved README documentation.
- Updated Python dependencies.
- Integrated npm package management (`package.json`, and lockfile).
- Updated `.gitignore` file.

### Removed
- Unnecessary `api\` application directory.

---

## [0.1.0] - 2026-04-23
([commit c66fb96](https://github.com/danilot390/Django_portfolio-AI/commit/c66fb96ebc3c795d8d62a6fbd1d4ccacdf57117d))

### Added
- Initial Django project setup.
- Modular app strucutre (`apps/`, `api/`).
- Environment variable configuration using `python-decouple`.
- Database  configuration via `dj-database-url`.
- Base dependency management with `requirements/` structure.
- Initial `.env` support for secure configuration.

### Configured 
- Default settings for `DEBUG` and `ALLOWED_HOSTS`.
- SQLite database for development environment.
- Project structure aligned for future scalability (AI modules, APIs)

### Notes
- This version establishes the foundational architecture for a scalable AI-driven portfolio platform.
