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



