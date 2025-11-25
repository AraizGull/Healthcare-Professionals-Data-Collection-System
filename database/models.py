# database/models.py — ONLY TABLE STRUCTURE
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base  
from datetime import datetime

Base = declarative_base()

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    npi = Column(String, unique=True, nullable=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)
    phone = Column(String)
    email = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    specialty = Column(String)
    license_number = Column(String)
    license_state = Column(String)
    source = Column(String, default="Manual")
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

print("[DB] models.py loaded → Doctor structure ready!")