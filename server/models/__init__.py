from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance

__all__ = ['db', 'User','Guest', 'Episode', 'Appearance']
