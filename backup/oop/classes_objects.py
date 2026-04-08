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