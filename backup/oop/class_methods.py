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

country = Country.from_api_response(api_data)

