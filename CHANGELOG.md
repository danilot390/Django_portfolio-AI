All notabel changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/)

---

## [0.2.0] - 10-05-2026
([commit ]())

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

## [0.1.0] - 23-04-2026
([commit c66fb96](https://github.com/danilot390/Django_portfolio-AI/commit/c66fb96ebc3c795d8d62a6fbd1d4ccacdf57117d))

### Added
- Initial Django project setup.
- Modular app strucutre (`apps/`, `api/`).
- Environment variable configuration using `python-decouple`.
- Database  configuration via `dj-database-url`.
- Base dependency managment with `requirements/` structure.
- Initial `.env` support for secure configuration.

### Configured 
- Default settings for `DEBUG` and `ALLOWED_HOSTS`.
- SQLite database for development environment.
- Project structure aligned for future scalability (AI modules, APIs)

### Notes
- This version establishes the foundational architecture for a scalable AI-driven portfolio platform.
