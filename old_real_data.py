# old_real_data.py 
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import text

# Connect directly without assuming any columns
engine = create_engine("sqlite:///doctors_real_live.db", connect_args={"check_same_thread": False})

print("="*100)
print("REAL LIVE SCRAPED US HEALTHCARE PROVIDERS: 1668 RECORDS")
print("FROM: doctors_real_live.db")
print("="*100)

try:
    with engine.connect() as conn:
        # First, get total count
        count_result = conn.execute(text("SELECT COUNT(*) FROM doctors"))
        total = count_result.scalar()
        print(f"TOTAL RECORDS IN DATABASE: {total}\n")
        
        # Now get first 25 records (raw way — no model needed)
        result = conn.execute(text("""
            SELECT npi, full_name, phone, city, state, specialty 
            FROM doctors 
            LIMIT 25
        """))
        
        rows = result.fetchall()
        
        for i, row in enumerate(rows, 1):
            npi = row[0] or "Unknown"
            name = row[1].strip() if row[1] and row[1].strip() else "Name not captured"
            phone = row[2].strip() if row[2] and row[2].strip() else "Not listed"
            city = row[3] or "Unknown"
            state = row[4] or ""
            specialty = row[5].strip() if row[5] and row[5].strip() else "General"
            
            print(f"{i:2}. NPI: {npi} | {name} | {city}, {state} | {specialty} | {phone}")

    
    print("="*100)

except Exception as e:
    
    print("Error details (for reference):", e)