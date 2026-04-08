

languages = ["German", "Danish", "Lower Sorbian", "North Frisian"]

print("Languages Spoken: ")
for lang in languages:
    print(f" - {lang}")

neighbours = ["AUT", "BEL", "CZE", "DNK", "FRA", "LUX", "NLD", "POL", "CHE"]

print(f" This country has {len(neighbours)} neighbours")
for i, code in enumerate (neighbours, 1):
    print(f" {i}. {code}")
