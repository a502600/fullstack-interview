import os
from dotenv import load_dotenv

load_dotenv()

# Database
DB_NAME = os.getenv("DB_NAME", "sqlite.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"

# CORS
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# API
X_API_KEY = os.getenv("X_API_KEY", "")
