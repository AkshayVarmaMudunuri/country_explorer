import math

def population_density(population, area_km2):
    if area_km2 == 0:
        return 0
    return round(population / area_km2, 1)

uk_density    = population_density(67000000, 243610)  
japan_density = population_density(125700000, 377930) 
russia_density= population_density(144100000,17098242)

print(f"UK:      {uk_density} people/km²")
print(f"Japan:   {japan_density} people/km²")
print(f"Russia:  {russia_density} people/km²")

uk_destiny = 275
if japan_density > uk_density:
    print(f"Japan is more densely populated than the UK")



