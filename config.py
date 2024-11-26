import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'UJLHHFDESTYF6797IUYKTFHH8P7O86T5RED45667FIVB7')
    
    # Check the value of FLASK_ENV environment variable
    FLASK_ENV = os.getenv('FLASK_ENV', 'development').lower()

    if FLASK_ENV == 'production':
        # Use production database URI from .env
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    else:
        # Use SQLite as a default for development
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///notes.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
