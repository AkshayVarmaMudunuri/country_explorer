
countries = [
    {"name": "Germany",  "population": 83200000},
    {"name": "Iceland",  "population":   372000},
    {"name": "France",   "population": 67400000},
    {"name": "Vatican",  "population":     800},
]

by_pop = sorted(countries, key= lambda c: c["population"], reverse=True)

name = list(map(lambda c: c["name"], countries))

large = list(filter(lambda c: c["population"] > 1_000_000, countries))
large_names = [c["name"] for c in large]

print("Largest:", by_pop[0]["name"])
print("Large countries:", large_names)


