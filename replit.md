# TeenVision API

## Overview
TeenVision is a Django REST API backend that connects high school students with educational programs, including summer schools, competitions, scholarships, and workshops. The platform makes valuable opportunities more accessible, organized, and tailored to students' interests, majors, and demographics.

**Current Status**: Fully operational in Replit environment
**Last Updated**: October 4, 2025

## Technology Stack
- **Framework**: Django 5.2
- **API Framework**: Django REST Framework 3.16.0
- **Authentication**: JWT (djangorestframework-simplejwt 5.5.0)
- **API Documentation**: drf-yasg (Swagger/OpenAPI)
- **Database**: SQLite (development), PostgreSQL (production)
- **Production Server**: Gunicorn 23.0.0
- **Python Version**: 3.11

## Project Structure
```
TeenVision/
├── config/              # Django project settings
│   ├── settings.py     # Main configuration
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI application
├── core/               # Core application
│   ├── migrations/     # Database migrations
│   ├── serializers/    # DRF serializers
│   └── views/          # API views
├── users/              # User management app
│   ├── migrations/     # User model migrations
│   └── models.py       # Custom user model
├── media/              # User-uploaded files
└── manage.py           # Django management script
```

## Recent Changes

### October 4, 2025 - Initial Replit Setup
- Installed Python 3.11 and all project dependencies
- Configured database with automatic fallback from PostgreSQL to SQLite
- Ran all Django migrations successfully
- Set up Django development server on port 5000
- Configured deployment with Gunicorn for production
- Verified API documentation (Swagger UI) is accessible

## Development Setup

### Database Configuration
The application uses a smart database configuration that:
1. Attempts to connect to PostgreSQL if credentials are available in `.env`
2. Automatically falls back to SQLite for development if PostgreSQL is unavailable
3. Uses the custom User model from the `users` app

### Running the Application
The server starts automatically via the configured workflow:
- **Development**: `python manage.py runserver 0.0.0.0:5000`
- **Production**: `gunicorn --bind=0.0.0.0:5000 --reuse-port config.wsgi:application`

### API Documentation
The API documentation is available at the root URL (`/`) using Swagger UI, providing:
- Interactive API exploration
- Authentication options (Django Login, JWT)
- Endpoint testing capabilities

## Key Features
- **JWT Authentication**: Secure token-based authentication with refresh tokens
- **User Management**: Custom user model with notification status
- **Program Management**: Core functionality for managing educational programs
- **Media Uploads**: Support for program photos and other media
- **API Filtering**: Django Filter integration for advanced querying
- **CORS Support**: Cross-origin resource sharing enabled for frontend integration

## Environment Variables
The following variables can be configured in `.env`:
- `SECRET_KEY`: Django secret key
- `POSTGRES_DB`: PostgreSQL database name
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_HOST`: PostgreSQL host
- `POSTGRES_PORT`: PostgreSQL port

## Deployment
The application is configured for autoscale deployment:
- Uses Gunicorn as the production WSGI server
- Automatically scales based on traffic
- Suitable for stateless API deployments
- Database state managed through PostgreSQL in production

## Security Settings
- `DEBUG = True` (development only)
- `ALLOWED_HOSTS = ['*']` (configured for Replit proxy)
- `CORS_ALLOW_ALL_ORIGINS = True` (development setting)
- JWT tokens with 30-minute access and 3-day refresh lifetime

## Next Steps
To continue development:
1. Create a superuser: `python manage.py createsuperuser`
2. Access Django admin at `/admin`
3. Explore API endpoints via Swagger UI at `/`
4. Configure PostgreSQL for production deployment
5. Update security settings (DEBUG, ALLOWED_HOSTS, CORS) for production
