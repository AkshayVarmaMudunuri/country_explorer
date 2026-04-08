
countries = ["Brazil", "Japan", "", "Germany", "France"]

print("Valid Country Found")
for country in countries:
    if not country:
        continue
    print(f" {country}")
    if country == "Germany":
        print("Found target country - stopping search")
        break

