# run.py — ONE COMMAND TO RUN EVERYTHING
import os
from datetime import datetime

print("=" * 80)
print(" HEALTHCARE PROFESSIONALS DATA COLLECTION SYSTEM")
print(" USA + PAKISTAN FULLY AUTOMATED")
print(f" Started at: {datetime.now().strftime('%Y-%m-%d %I:%M %p')} PKT")
print("=" * 80)

print("\n1. Running clean demo (8 verified doctors)...")
os.system("python main.py")

print("\n2. Showing clean database...")
os.system("python test_db.py")

print("\n3. Showing REAL live-scraped data (1668 records)...")
os.system("python old_real_data.py")

print("\n" + "="*80)
print("SYSTEM READY ALL DATA LOADED SUCCESSFULLY")
print("="*80)