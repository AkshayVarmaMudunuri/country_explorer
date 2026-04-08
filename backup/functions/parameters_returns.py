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
