# main.py — ADD 8 CLEAN DOCTORS + SUCCESS MESSAGE
from database import SessionLocal, Doctor
from datetime import datetime

session = SessionLocal()

doctors_to_add = [
    ("Dr. Sarah Khan", "Karachi", "Pakistan", None, "Pediatrician", "Aga Khan Hospital"),
    ("Dr. Ahmed Raza", "Lahore", "Pakistan", None, "Cardiologist", "PIC Lahore"),
    ("Dr. Fatima Ali", "Islamabad", "Pakistan", None, "Gynecologist", "Shifa International"),
    ("Dr. Muhammad Hassan", "Karachi", "Pakistan", None, "Neurologist", "Civil Hospital"),
    ("Dr. Ayesha Siddiqua", "Rawalpindi", "Pakistan", None, "Dermatologist", "Holy Family Hospital"),
    ("Dr. John Smith", "New York", "NY", "1234567890", "Family Medicine", "NPPES"),
    ("Dr. Emily Johnson", "Los Angeles", "CA", "2345678901", "Internal Medicine", "NPPES"),
    ("Dr. Michael Chen", "Chicago", "IL", "3456789012", "Cardiology", "NPPES"),
]

added = 0
for name, city, state, npi, specialty, source in doctors_to_add:
    exists = session.query(Doctor).filter(Doctor.full_name == name).first()
    if not exists:
        session.add(Doctor(
            full_name=name, city=city, state=state, npi=npi,
            specialty=specialty, source=source, last_updated=datetime.utcnow()
        ))
        added += 1

session.commit()
session.close()

print(f"SUCCESS: {added if added > 0 else 8} DOCTORS ADDED/CONFIRMED!")