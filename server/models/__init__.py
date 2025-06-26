from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models so Alembic can detect them
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance
