
def show_country(country, detailed= False):

    print(f"  {country['name']} {country.get('flag_emoji','')}")
    print(f"  Capital: {country['capital']}")
    print(f"  Population: {country['population']:,}")

    if detailed:
        print(f"  Area: {country['area_km2']:,.0f} km²")
        print(f"  Language: {', '.join(country['languages'])}")
        print(f"  Currency: {country['currency']}")
        print(f"  Region: {country['region']}")

show_country(japan_data)
show_country(japan_data, detailed= True)

