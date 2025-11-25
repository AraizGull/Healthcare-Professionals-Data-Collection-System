# test_db.py
from database.db import SessionLocal
from database.models import Doctor
from datetime import datetime

print("\n" + "="*80)
print(" HEALTHCARE PROFESSIONALS DATABASE USA + PAKISTAN")
print("="*80)

session = SessionLocal()
doctors = session.query(Doctor).all()
session.close()

if not doctors:
    print("No doctors found in database.")
    print("Run: python main.py to add doctors first.")
else:
    print(f"TOTAL DOCTORS: {len(doctors)}\n")
    for i, doc in enumerate(doctors, 1):
        npi_info = f"NPI: {doc.npi}" if doc.npi else "No NPI (Pakistan)"
        print(f"{i:2}. {doc.full_name:<30} | {doc.city:<15} | {doc.specialty:<20} | {npi_info}")
        print(f"     Source: {doc.source} | Updated: {doc.last_updated.strftime('%Y-%m-%d')}")
        print("   " + "─" * 76)

print(f"\nQuery completed at {datetime.now().strftime('%Y-%m-%d %I:%M %p')} PKT")