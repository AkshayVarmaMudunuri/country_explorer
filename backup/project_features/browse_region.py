from api.countries import get_countries_in_region

REGIONS = ["Africa", "Americas", "Asia", "Europe", "Oceania"]

def browse_region():
    print("Available Regions:")
    for i, r in enumerate(REGIONS, 1):
        print(f" {i}. {r}")

    region = input("Enter the Region: ").strip()

    if region not in REGIONS:
        print(f" Try one of: {', '.join(REGIONS)}")
        return

    print(f" fetching countries in {region}..")
    countries = get_countries_in_region(region)

    if not countries:
        print(" No result found.")
        return

    countries.sort()
    print(f" {region} - {len(countries)} countries:")

    for i, name in enumerate(countries, 1):
        print(f" {i:3}. {name}")








