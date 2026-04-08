
countries = [
    ("Germany",  83200000),
    ("France",   67400000),
    ("Poland",   38000000),
    ("Greece",   10700000),
]

max_pop = max(pop for _, pop in countries)

print(f" {'Countries':<15} {'Population':>15}    Chart")
print("-" * 50)

for name, pop in countries:
    bar_len = round((pop / max_pop) * 25)
    bar = "█" * bar_len

    print(f"{name:<15} {pop:>15,}    {bar}")

    