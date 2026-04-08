def get_country_with_feedback(name):
    
    if not name or not name.strip():
        print("  Please type a country name and press Enter.")
        return None 

    if len(name.strip()) < 2:
        print(f"  '{name}' is too short — try a full country name.")
        return None

    if any (c.isdigit() for c in name):
        print(f"  '{name}' contains numbers — country names don't have numbers.")
        return None

    country = get_country(name)

    if country is None:
        print(f"  '{name}' not found.")
        print(f"  Tip: try the English name, e.g. 'Germany' not 'Deutschland'")
        print(f"  Or try 'United Kingdom' instead of 'UK'")

    return country  


