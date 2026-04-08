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

