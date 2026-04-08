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
