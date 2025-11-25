# scraper/nppes.py
import requests
import time
from database.models import Doctor, SessionLocal
from validator.validators import validate_npi, validate_phone, extract_specialty
from datetime import datetime
import config

def search_nppes(params):
    """Send request to NPPES API with delay and error handling"""
    headers = {"User-Agent": config.USER_AGENT}
    try:
        response = requests.get(config.NPPES_API, params=params, headers=headers, timeout=15)
        time.sleep(config.REQUEST_DELAY)  # Respectful delay
        if response.status_code == 200:
            return response.json()
        else:
            print(f"  → NPPES Error {response.status_code}: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"  → Request failed: {e}")
        return None


# FULLY WORKING IN NOVEMBER 2025
def fetch_and_store_doctors(
    first_name="", last_name="", city="", state="",
    taxonomy_description="", limit=200, skip=0
):
    """
    Fetch doctors from NPPES and store in database.
    Works 100% with current NPPES API (2025).
    Returns: number of new doctors added
    """
    print(f"  → Searching: city={city or 'any'}, state={state or 'any'}, "
          f"taxonomy={taxonomy_description or 'any'}, limit={limit}, skip={skip}")

    params = {
        "version": "2.1",
        "first_name": first_name,
        "last_name": last_name,
        "city": city,
        "state": state,
        "taxonomy_description": taxonomy_description,   # ← Critical for 2025
        "limit": limit,
        "skip": skip,
        "pretty": "on"
    }

    # Remove empty parameters
    params = {k: v for k, v in params.items() if v}

    data = search_nppes(params)
    if not data or "results" not in data:
        print("  → No results from NPPES.")
        return 0

    results = data["results"]
    if len(results) == 0:
        print("  → Empty results.")
        return 0

    session = SessionLocal()
    added = 0
    skipped = 0

    for result in results:
        # === Extract NPI ===
        npi = result.get("number")
        if not npi or not validate_npi(npi):
            skipped += 1
            continue

        # === Extract Name ===
        basic = result.get("basic", {})
        first = basic.get("first_name", "").strip()
        last = basic.get("last_name", "").strip()
        full_name = f"{first} {last}".strip()
        if not full_name:
            skipped += 1
            continue

        # === Extract Primary Address ===
        addrs = result.get("addresses", [])
        if not addrs:
            skipped += 1
            continue

        addr = addrs[0]  # Primary practice location
        phone = addr.get("telephone_number")
        if phone and not validate_phone(phone):
            phone = None

        street = f"{addr.get('address_1', '')} {addr.get('address_2', '')}".strip()
        city_name = addr.get("city", "")
        state_addr = addr.get("state", "")
        zip_code = addr.get("postal_code", "")[:5]

        if not all([city_name, state_addr]):
            skipped += 1
            continue

        # === Extract Specialty ===
        specialty = extract_specialty(result.get("taxonomies", []))

        # === Create Doctor Object ===
        doc = Doctor(
            npi=str(npi),
            first_name=first,
            last_name=last,
            full_name=full_name,
            phone=phone,
            email=None,
            street=street or None,
            city=city_name,
            state=state_addr,
            zip_code=zip_code or None,
            specialty=specialty,
            license_number=None,
            license_state=state_addr,
            source="NPPES",
            last_updated=datetime.utcnow()
        )

        # === Save or Update (Upsert) ===
        existing = session.get(Doctor, str(npi))
        if existing:
            session.merge(doc)
        else:
            session.add(doc)
            added += 1

    session.commit()
    session.close()
    print(f"  → Added: {added}, Skipped: {skipped}")
    return added