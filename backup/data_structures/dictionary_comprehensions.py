
countries = [
    {"name": "Germany",  "population": 83200000,  "capital": "Berlin"},
    {"name": "France",   "population": 67400000,  "capital": "Paris"},
    {"name": "Poland",   "population": 38000000,  "capital": "Warsaw"},
]

pop_lookup = {c["name"]: c["population"] for c in countries}
print(pop_lookup["Germany"])

capital_lookup = {c["name"]: c["capital"] for c in countries}
print(capital_lookup["France"])

large = {c["name"]: c["population"]
        for c in countries 
        if c["population"] > 50_000_000}

print(large)