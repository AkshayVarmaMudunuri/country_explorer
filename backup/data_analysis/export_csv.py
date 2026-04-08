import pandas as pd
import json

def export_cache_to_csv():
    try:
        with open("data/cache.json") as f:
            cache = json.load(f)
    except FileNotFoundError:
        print("No cached data yet. Look up some countries first.")
        return

    records =[]
    for name, data in cache.items():
        records.append({
            "Country":    data.get("name", name),
            "Capital":    data.get("capital", ""),
            "Population": data.get("population", 0),
            "Region":     data.get("region", ""),
            "Area (km²)": data.get("area_km2", 0),
        })
    df = pd.DataFrame(records)
    df.to_csv("reports/countries.csv", index=False)

    print(f" Exported {len(records)} countries to reports/countries.csv")