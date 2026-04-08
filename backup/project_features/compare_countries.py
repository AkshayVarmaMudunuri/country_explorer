from api.countries import get_country
from utils.display import show_comparison

def compare():
    print("Compare two countries")
    name1 = input(" First country: ").strip()
    name2 = input(" Second country: ").strip()

    print(f" Fetching {name1}...")
    c1 = get_country(name1)

    print(f" Fetching {name2}...")
    c2 = get_country(name2)

    if not c1 or not c2:
        print(" Could not fetch one or both countries.")
        return 

    show_comparison(c1, c2)

    pop_diff =  abs(c1["population"] - c2["population"])
    print(f"  Population difference: {pop_diff:,} people")

    area_ratio = c1["area_km2"] / c2["area_km2"] if c2["area_km2"] else 0
    print(f" {c1['name']} is {area_ratio:.1f}x the size of {c2['name']}")





