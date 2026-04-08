def region_facts(countries_data):
    if not countries_data:
        return

    largest_pop = max(countries_data, key=lambda c: c["population"])
    print(f"  Most populated: {largest_pop['name']} ({largest_pop['population']:,})")

    smallest_pop = min(countries_data, key=lambda c: c["population"])
    print(f"  least populated: {smallest_pop['name']} ({smallest_pop['population']:,})")

    largest_area = max(countries_data, key=lambda c: c["area_km2"])
    print(f" Largest by area: {largest_area['name']} ({largest_area['area_km2']:,.0f} km²)")

    avg = sum(c["population"] for c in countries_data) // len(countries_data)
    print(f" Average population: {avg:,}")




