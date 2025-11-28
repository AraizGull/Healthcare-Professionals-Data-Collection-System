# add_pakistan.py 
from scraper.utils import scrape_hospital_doctors

print("ADDING REAL PAKISTANI DOCTORS (LIVE 2025)")
print("="*60)
total = 0
total += scrape_hospital_doctors("Shaukat Khanum", max_pages=5)
total += scrape_hospital_doctors("Shifa International", max_pages=5)
print("="*60)
print(f"SUCCESS → {total} REAL PAKISTANI DOCTORS ADDED!")
print("Now run: python test_db.py to see them!")