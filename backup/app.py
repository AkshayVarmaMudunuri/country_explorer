
country_name = "Japan"
population   = 125700000
area_km2     = 377930.0
is_island    = True


print(f"Country:  {country_name}")
print(f"Population:  {population:,}")
print(f"Area:  {area_km2:,.1f} km²")
print(f"Island:  {is_island}")


country_name = input("Enter the Country name: ")
country_name = country_name.strip().title()

print(f"You entered:  {country_name}")
print(f"Looking up  {country_name}....")


name       = "Japan"
population = 125700000
area_km2   = 377930.0
capital    = "Tokyo"

print(f"{'Population':<12} {population:,}")
print(f"{'Area':<12} {area_km2:,.1f} km²")
print(f"{'Country':<12} {name}")
print(f"{'Capital':<12} {capital}")



name = input("Enter the Country: ").strip()

if len(name) < 2:
    print("Too short - please enter full country name")
elif any(char.isdigit() for char in name):
    print("country name don't contain numbers")
else:
    print(f"Looking up {name}...")


population = 125700000

if population > 1_000_000_000:
    print("Highly Populated Country")
elif population > 100_000_000:
    print("Large Country by population")
elif population > 10_000_000:
    print("Medium Sized Country")
else:
    print("Smaller Country by Population")


languages = ["German", "Danish", "Lower Sorbian", "North Frisian"]

print("Languages Spoken: ")
for lang in languages:
    print(f" - {lang}")

neighbours = ["AUT", "BEL", "CZE", "DNK", "FRA", "LUX", "NLD", "POL", "CHE"]

print(f" This country has {len(neighbours)} neighbours")
for i, code in enumerate (neighbours, 1):
    print(f" {i}. {code}")



print("Country Explorer - type 'q' to quit")

while True:
    name = input("Enter the country name: ").strip()

    if name.lower() == "q":
        print("Good Bye!")
        break

    if not name:
        print("Please Type Country name:")
        continue

    print(f" looking up {name.title()}...")


    countries = ["Brazil", "Japan", "", "Germany", "France"]

    print("Valid Country Found")
    for country in countries:
        if not country:
            continue
        print(f" {country}")
        if country == "Germany":
            print("Found target country - stopping search")
            break



    def show_country_basic(name, capital, population):

        print("=" * 35)
        print(f"   {name.upper()}")
        print(f"   Capital:    {capital}")
        print(f"   Population: {population:,}")
        print("=" * 35)

    show_country_basic("Japan", "Toyko", 125700000)
    show_country_basic("Germany", "Berlin",  83200000)
    show_country_basic("Brazil",  "Brasília",215300000)

    def formate_population(number):
        if number >= 1_000_000_000:
            return f"{number/1_000_000_000:.1f} billion"
        elif number >= 1_000_000:
            return f"{number/1_000_000:.1f} million"
        else:
            return f"{number:,}"

    def is_large_country(area_km2):
        return area_km2 > 1_000_000

    pop_str = formate_population(125700000)
    print(f"Population: {pop_str}")

    big = is_large_country(377930)
    print(f"Large Country: ({big})")

    def show_country(country, detailed= False):

        print(f"  {country['name']} {country.get('flag_emoji','')}")
        print(f"  Capital: {country['capital']}")
        print(f"  Population: {country['population']:,}")

        if detailed:
            print(f"  Area: {country['area_km2']:,.0f} km²")
            print(f"  Language: {', '.join(country['languages'])}")
            print(f"  Currency: {country['currency']}")
            print(f"  Region: {country['region']}")

    #show_country(japan_data)
   # show_country(japan_data, detailed= True)



def country(name):
    pass

history = []

history.append("Japan")
history.append("Germany")
history.append("Brazil")

print(f"You searched {len(history)} countries:")

for i, country in enumerate(history,1):
    print(f" {i}. {country}")

print(f"First Search:  {history[0]}")
print(f"Last Search:   {history[-1]}")

if "Japan" in history:
    print("Japan is in your history")

raw_api_data = {
    "name":       {"common": "Japan", "official": "Japan"},
    "capital":    ["Tokyo"],
    "population": 125700000,
    "languages":  {"jpn": "Japanese"},
    "currencies": {"JPY": {"name": "Japanese yen", "symbol": "¥"}},
    "borders":    [],
    "flag":       "🇯🇵"
}

name = raw_api_data["name"]["common"]
capital = raw_api_data["capital"][0]
language = list(raw_api_data["languages"].values())[0]
currency = raw_api_data["currencies"]["JPY"]["name"]

region = raw_api_data.get("region", "Unknown")


VALID_REGIONS = (
    "Africa", "Americas", "Asia",
    "Europe", "Oceania", "Antarctic"
)

region = input("Enter the region: ").strip()
if region in VALID_REGIONS:
    print(f" Valid region: {region}")

else:
    print(f" Valid option: {', '.join (VALID_REGIONS)}")

searched = set()

searched.add("Japan")
searched.add("Germany")
searched.add("Japan")
searched.add("Brazil")

print(f" Unique Countries {len(searched)}")
print(searched)

countries = [
    {"name": "Germany", "population": 83200000, "area": 357114},
    {"name": "France",  "population": 67400000, "area": 551695},
    {"name": "Iceland", "population":   372000, "area": 103000},
    {"name": "Russia",  "population":144100000, "area":17098242},
]

name = [c["name"] for c in countries]

large = [c["name"] for c in countries if c["population"] > 50_000_000]

formatted = [f"{c['name']}: {c['population']:,}" for c in countries]



import requests

def get_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url, timeout=10)

    print(f'Status code: {response.status_code}')

    data = response.json()
    country = data[0]
    return country

result = get_country("Japan")
print(result["name"]["common"])
print(result["capital"][0])


import requests

def get_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print(f"'{name}' not found. Check the Spelling.")
            return None

        response.raise_for_status()
        data = response.json()
        return data[0]

    except requests.exception.ConnectionError:
        print("No internet connection. Check your WiFi.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
        return None


import json
import os

CACHE_FILE = "data/cache.json"

def load_cache():
    os.makedirs("data", exist_ok= True)
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

cache = load_cache()

if "japan" in cache:
    country = cache["japan"]
else:
    country = get_country("japan")
    cache["japan"] = country
    save_cache(cache)

import os

if os.path.exists("data/cache.json"):
    print("Cache file found")

else:
    print("No cache yet")

os.makedirs("data", exist_ok= True)
os.makedirs("reports", exist_ok=True)

filename = os.path.join("reports", "japan_report.txt")
print(filename)

class Country:

    def __init__(self, name, capital, population, region, languages, currency, flag_emoji, area_km2):
        self.name        = name
        self.capital     = capital
        self.population  = population
        self.region      = region
        self.languages   = languages
        self.currency    = currency
        self.flag_emoji  = flag_emoji
        self.area_km2    = area_km2

japan = Country(
    name="Japan", 
    capital="Tokyo", 
    population=125700000, 
    region="Asia", 
    languages=["Japanese"], 
    currency="Yen (¥)", 
    flag_emoji="🇯🇵", 
    area_km2=377930
)

print(japan.name)
print(japan.population)

class Country:

    def __init__(self, name, capital, population, languages):
        self.name        = name
        self.capital     = capital
        self.population  = population
        self.languages   = languages

    def display(self):
        print(f" {self.name}")
        print(f" Capital:    { self.capital}")
        print(f" Population: { self.format_population()}")
        print(f" Language:   {', '.join(self.languages)}")

    def format_population(self):
        if self.population >= 1_000_000_000:
            return f"{self.population/1_000_000_000:.1f} billion"
        return f"{self.population/1_000_000:.1f} million"

    def to_dict(self):
        return {"name": self.name , "capital": self.capital, "population": self.population}

japan = Country("Japan", "Tokyo", 125700000, ["Japanese"])
japan.display() 

class Country:

    def __init__(self, name, capital, population, languages, currency, flag_emoji, area_km2, neighbours):
        self.name        = name
        self.capital     = capital
        self.population  = population
        self.languages   = languages
        self.currency    = currency
        self.flag_emoji  = flag_emoji
        self.area_km2    = area_km2
        self.neighbours  = neighbours

    @classmethod
    def from_api_response(cls, data):
        langs = list(data.get("languages", {}).values())
        curr = list(data.get("currencies", {}).values())
        curr_str = f"{curr[0]['name']} ({curr[0].get('symbol','')})" if curr else "Unknown"

        return cls(
            name       = data["name"]["common"],
            capital    = data.get("capital", ["Unknown"])[0],
            population = data.get("population", 0),
            languages  = langs,
            currency   = curr_str,
            flag_emoji = data.get("flag", ""),
            area_km2   = data.get("area", 0),
            neighbours = data.get("borders", []),
        )

#country = Country.from_api_response(api_data)

class Country:
    def __init__(self, name, capital, population,):
        self.name       = name
        self.capital    = capital
        self.population  = population

    def describe(self):
        return f"{self.name}, capital {self.capital}"

class SovereignCountry(Country):
    def __init__(self, name, capital, population, un_member):
        super().__init__(name, capital, population)
        self.un_member = un_member

    def describe(self):
        base = super().describe()
        status = "UN member" if self.un_member else "observer"
        return f"{base} ({status})"

japan = SovereignCountry("Japan", "Tokyo", 125700000, True)
print(japan.describe())



import math

def population_density(population, area_km2):
    if area_km2 == 0:
        return 0
    return round(population / area_km2, 1)

uk_density    = population_density(67000000, 243610)  
japan_density = population_density(125700000, 377930) 
russia_density= population_density(144100000,17098242)

print(f"UK:      {uk_density} peopel/km²")
print(f"Japan:   {japan_density} people/km²")
print(f"Russia:  {russia_density} people/km²")

uk_destiny = 275
if japan_density > uk_density:
    print(f"Japan is more densely populated than the UK")


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


raw = " united kingdom "
clean = raw.strip().title()

print("japan".capitalize())
print("JAPAN".lower())
print("japan".upper())

print("japan123".isalpha())
print("japan".isalpha())


languages = ["German", "French", "Italian"]
joined = ", ".join(languages)
print(joined)

text = "Tokyo,Seoul,Beijing"
cities = text.split(",")


from api.countries import get_country, get_countries_in_region
from utils.display import show_countries, show_comparison
from utils.validator import is_valid_country_name, clean_name

import os
import json
from datetime import date
import requests 


countries = [
    {"name": "Germany",  "population": 83200000},
    {"name": "Iceland",  "population":   372000},
    {"name": "France",   "population": 67400000},
    {"name": "Vatican",  "population":     800},
]

by_pop = sorted(countries, key=lambda c: c["population"], reverse=True)

name = list(map(lambda c: c["name"], countries))

large = list(filter(lambda c: c["population"] > 1_000_000, countries))
large_names = [c["name"] for c in large]

print("Largest:", by_pop[0]["name"])
print("Large countries:", large_names)


countries = [
    ("Germany",  83200000),
    ("France",   67400000),
    ("Poland",   38000000),
    ("Greece",   10700000),
]

max_pop = max(pop for _, pop in countries)

print(f" {'Countries':<15} {'Population':>15} Chart")
print("-" * 50)

for name, pop in countries:
    bar_len = round((pop / max_pop) * 25)
    bar = "█" * bar_len

    print(f"{name:<15} {pop:>15,} {bar}")




countries = [
    {"name": "Germany",  "population": 83200000,  "capital": "Berlin"},
    {"name": "France",   "population": 67400000,  "capital": "Paris"},
    {"name": "Poland",   "population": 38000000,  "capital": "Warsaw"},
]

pop_lookup = {c["name"]: c["population"] for c in countries}
print(pop_lookup["Germany"])

captial_lookup = {c["name"]: c["capital"] for c in countries}
print(captial_lookup["France"])

large = {c["name"]: c["population"]
        for c in countries 
        if c["population"] > 50_000_000}

print(large)

def get_country_with_feedback(name):
    
    if not name or not name.strip():
        print("  Please type a country name and press Enter.")
        return None 

    if len(name.strip()) < 2:
        print(f"  '{name}' is too short — try a full country name.")
        return None

    if any (c.isdigit() for c in name):
        print(f"  '{name}' contains numbers — country names don't have numbers.")
        return None

    country = get_country(name)

    if country is None:
        print(f"  '{name}' not found.")
        print(f"  Tip: try the English name, e.g. 'Germany' not 'Deutschland'")
        print(f"  Or try 'United Kingdom' instead of 'UK'")

    return country  


from api.countries import get_country
from utils.display import show_comparison

def compare():
    print("Compare two countries")
    name1 = input(" First country: ").strip()
    name2 = input(" Second country: ").strip()

    print(f" Fetching {name1}...")
    c1 = get_country(name1)

    print(f" Fetching {name2}...")
    c2 = get_country(name2)

    if not c1 or not c2:
        print(" Could not fetch one or both countries.")
        return 

    show_comparison(c1, c2)

    pop_diff =  abs(c1["population"] - c2["population"])
    print(f"  Population difference: {pop_diff:,} people")

    area_ratio = c1["area_km2"] / c2["area_km2"] if c2["area_km2"] else 0
    print(f" {c1['name']} is {area_ratio:.1f}x the size of {c2['name']}")

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

import os 
from datetime import date

def save_report(country):
    os.makedirs("reports", exist_ok=True)

    today = date.today().strftime("%Y-%m-%d")
    safe_name = country["name"].replace(" ", "_")
    filename = f"reports/{safe_name}_{today}.txt"

    lines = [
        f"Country Explorer Report",
        f"Generated: {today}",
        f"{'=' * 40}",
        f"Country:    {country['name']}",
        f"Capital:    {country['capital']}",
        f"Population: {country['population']:,}",
        f"Region:     {country['region']}",
        f"Languages:  {', '.join(country['languages'])}",
        f"Currency:   {country['currency']}",
    ]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".json(lines))

    print(f"  Report saved: {filename}")



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




import matplotlib.pyplot as plt

names  = ["Germany", "France", "Poland", "Greece"]
pops   = [83200000, 67400000, 38000000, 10700000]

pop_m = [p/ 1_000_000 for p in pops]

plt.figure(figsize = (10,5))
bars = plt.bar(names, pop_m, color="#F03612")
plt.title(" Population by countries (Millions) ")
plt.ylabel(" Population in Millions ")
plt.xlabel(" Country ")

for bar, val in zip(bars, pop_m):
    plt.text(bar.get_x() + bar.get_width()/2,
    bar.get_height() + 0.5,
    f"{val:.1f}M", ha="center")

plt.tight_layout()
plt.savefig("reports/population_chart.png", dpi=150)
plt.show()
print("Chart saved to reports/population_chart.png")

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


import pandas as pd
import json

def export_cache_to_csv():
    try:
        with open("data/cache.json") as f:
            cache = json.load(f)
    except FileNotFoundError:
        print("No cached data yet. Look up some countries first.")
        return

    records =[]
    for name, data in cache.items():
        records.append({
            "Country":    data.get("name", name),
            "Capital":    data.get("capital", ""),
            "Population": data.get("population", 0),
            "Region":     data.get("region", ""),
            "Area (km²)": data.get("area_km2", 0),
        })
    df = pd.DataFrame(records)
    df.to_csv("reports/countries.csv", index=False)

    print(f" Exported {len(records)} countries to reports/countries.csv")

from utils.validator import is_valid_country_name, clean_name
from utils.display import format_population 

def test_valid_name_returns_true():
    assert is_valid_country_name("Japan") == True

def test_empty_name_returns_false():
    assert is_valid_country_name("") == False

def test_name_with_numbers_returns_false():
    assert is_valid_country_name("Japan123") == False

def test_clean_name_strips_spaces():
    assert clean_name(" japan ") == "Japan"

def test_clean_name_title_cases():
    assert clean_name( "united kingdom" ) == "United Kingdom"

def test_get_country_returns_correct_name(mocker):

    fake_api_data = [{

        "name":       {"common": "Japan", "official": "Japan"},
        "capital":    ["Tokyo"],
        "population": 125700000,
        "languages":  {"jpn": "Japanese"},
        "currencies": {"JPY": {"name": "Japanese yen", "symbol": "¥"}},
        "borders":    [],
        "flag":       "🇯🇵",
        "area":       377930,
        "region":     "Asia",
        "subregion":  "Eastern Asia",
        "timezones":  ["UTC+09:00"],
        "independent": "kw">True,
        "flags":      {"png": "https://flagcdn.com/jp.png"}

    }]

    mocker.patch("api.countries.requests.get",
    return_value = mocker.Mock(
        status_code = 200,
        json=lambda: fake_api_data
    ))

    from api.countries import get_country
    result = get_country("Japan")
    assert result["name"] == "Japan"
    assert result["capital"] == "Tokyo"
    assert result["population"] == 125700000


def test_very_long_name_is_invalid():
    long_name = "A" * 101
    assert is_valid_country_name(long_name) == False

def test_single_character_is_invalid():
    assert is_valid_country_name("A") == False

def test_spaces_only_is_invalid():
    assert is_valid_country_name("  ") == False

def test_valid_two_char_name():
    assert is_valid_country_name("UK") == True

def test_country_with_no_neighbours():
    from api.countries import get_country

country = {"name": "Japan", "neighbours": []}
neighbours_str = ", ".join(country["neighbours"]) or " None (island nation)"
assert neighbours_str == " None (island nation)"

