# validator/validators.py
import re
import phonenumbers

def validate_npi(npi):
    """Validate 10-digit NPI using Luhn algorithm"""
    if not npi or not re.match(r'^\d{10}$', str(npi)):
        return False
    digits = [int(d) for d in str(npi)]
    for i in range(len(digits)-2, -1, -2):  # Process every second digit from right
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits) + 24  # 24 is the fixed prefix for NPI
    return total % 10 == 0

def validate_phone(phone):
    """Validate US phone number"""
    if not phone:
        return False
    try:
        parsed = phonenumbers.parse(phone, "US")
        return phonenumbers.is_valid_number(parsed)
    except:
        return False

def extract_specialty(taxonomies):
    """Get primary specialty from taxonomies list"""
    if not taxonomies:
        return "Unknown"
    for t in taxonomies:
        if t.get("primary"):
            return t.get("desc", "Unknown")
    return taxonomies[0].get("desc", "Unknown")