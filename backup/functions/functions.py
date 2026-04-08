
def show_country_basic(name, capital, population):

    print("=" * 35)
    print(f"   {name.upper()}")
    print(f"   Capital:    {capital}")
    print(f"   Population: {population:,}")
    print("=" * 35)

show_country_basic("Japan", "Toyko", 125700000)
show_country_basic("Germany", "Berlin",  83200000)
show_country_basic("Brazil",  "Brasília",215300000)
