
countries = [
    {"name": "Germany", "population": 83200000, "area": 357114},
    {"name": "France",  "population": 67400000, "area": 551695},
    {"name": "Iceland", "population":   372000, "area": 103000},
    {"name": "Russia",  "population":144100000, "area":17098242},
]

name = [c["name"] for c in countries]

large = [c["name"] for c in countries if c["population"] > 50_000_000]

formatted = [f"{c['name']}: {c['population']:,}" for c in countries]