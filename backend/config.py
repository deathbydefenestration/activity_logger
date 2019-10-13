import os

# Sets the directory where the project runs
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode: also enables auto-reload upon saving
DEBUG = True

# Secret key for session management.
SECRET_KEY = 'fireman_sam'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# Turn off SQLAlchemy Track Modifications (when not using the event/hook system)
SQLALCHEMY_TRACK_MODIFICATIONS = False
