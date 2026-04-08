import pandas as pd

countries = [
    {"name": "Germany", "region": "Europe", "population": 83200000},
    {"name": "France",  "region": "Europe", "population": 67400000},
    {"name": "Japan",   "region": "Asia",   "population":125700000},
    {"name": "India",   "region": "Asia",   "population":1407563842},
    {"name": "Nigeria", "region": "Africa", "population":213401323},
]

df = pd.DataFrame(countries)

summary = df.groupby("region")["population"].agg(
    
    total = "sum",
    average = "mean",
    count = "count"
)
print(summary.sort_values("total", ascending=False).to_string())