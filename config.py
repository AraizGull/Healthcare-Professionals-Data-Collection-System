# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# SQLite database (file will be created automatically)
DATABASE_URL = "sqlite:///./doctors.db"

# NPPES API
NPPES_API = "https://npiregistry.cms.hhs.gov/api/"

# Be respectful
REQUEST_DELAY = 1.0
USER_AGENT = "HealthcareDataCollector/1.0 (+https://example.com)"


DATABASE_URL = "sqlite:///doctors_clean.db"   # ← NEW clean demo database