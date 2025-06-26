LATE SHOW API - FLASK BACKEND PROJECT

DESCRIPTION:
This is a RESTful API for managing data related to a Late Show. The application is built with Flask and provides endpoints to interact with guests, shows, and appearances.

PROJECT STRUCTURE:
- server/
  - __init__.py           # App and database initialization
  - app.py                # App entry point and route registration
  - models.py             # SQLAlchemy models for Guest, Show, Appearance
  - routes.py             # Controller functions and route handlers
  - seed.py               # Script to populate the database with sample data
  - config.py             # Application configuration

DEPENDENCIES:
- Python 3.12+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Faker (for sample data)

SETUP INSTRUCTIONS:
1. Clone the repository.

2. Navigate into the server directory:
   cd late-show-code-challenge/server

3. Create a virtual environment:
   python3 -m venv venv

4. Activate the virtual environment:
   source venv/bin/activate

5. Install the required packages:
   pip install -r requirements.txt

6. Set up and migrate the database:
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

7. Seed the database:
   python3 -m server/seed

8. Run the Flask application:
   python3 -m server.app

API ROUTES:

GUEST ROUTES:
GET /guests                  - List all guests
GET /guests/<id>             - Get a specific guest
POST /guests                 - Create a new guest
PATCH /guests/<id>           - Update a guest
DELETE /guests/<id>          - Delete a guest

SHOW ROUTES:
GET /shows                   - List all shows
GET /shows/<id>              - Get a specific show
POST /shows                  - Create a new show
PATCH /shows/<id>            - Update a show
DELETE /shows/<id>           - Delete a show

APPEARANCE ROUTES:
GET /appearances             - List all guest appearances
POST /appearances            - Create a guest appearance
GET /appearances/<id>        - Get a specific appearance

RESPONSE FORMAT:
All endpoints return JSON responses.

TESTING:
You can test API functionality using:
- Thunder Client (VS Code extension)
- Postman (free version)

NOTES:
- Always activate your virtual environment before running the server or other scripts.
- If using SQLite, the database will be created in the server/ directory.
- Run migrations any time you change the models.

AUTHOR:
Benson Kariuki

Github username:
munge124
# phase-4-code-challenge-2
