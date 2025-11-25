# database/db.py — CONNECTION & INITIALIZATION
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import config
import os

engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal
    
    db_path = config.DATABASE_URL.replace("sqlite:///", "")
    folder = os.path.dirname(db_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    
    engine = create_engine(
        config.DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    print(f"[DB] Connected → {config.DATABASE_URL}")
    print("[DB] SessionLocal READY!")

# Auto initialize when imported
init_db()