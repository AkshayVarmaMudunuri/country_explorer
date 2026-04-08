import pandas as pd

countries = [
    {"name": "Germany", "population": 83200000, "area": 357114},
    {"name": "France",  "population": 67400000, "area": 551695},
    {"name": "Poland",  "population": 38000000, "area": 312685},
    {"name": "Greece",  "population": 10700000, "area": 131957},
]


df = pd.DataFrame(countries)
print(df)

print(f" Total Countries: {len(df)}")
print(f"Total population: {df['population'].sum():,}")
print(f"Average population: {df['population'].mean():,.0f}")
print(f"Largest: {df.loc[df['population'].idxmax(), 'name']}")