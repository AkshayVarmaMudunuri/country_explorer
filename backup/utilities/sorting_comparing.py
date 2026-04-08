countries = [
    {"name": "France",  "population": 67400000, "area": 551695},
    {"name": "Germany", "population": 83200000, "area": 357114},
    {"name": "Iceland", "population":   372000, "area": 103000},
    {"name": "Russia",  "population":144100000, "area":17098242},
]


by_population = sorted(countries, key= lambda c: c["population"], reverse=True)

print("By population (largest first):")

for i, c in enumerate(by_population, 1):
    print(f" {i}. {c['name']:15} {c['population']:>15,}")

by_name = sorted(countries, key= lambda c: c["name"])
names_only = [c["name"] for c in by_name]

print(f" Alphabetical: {', '.join(names_only)}")


