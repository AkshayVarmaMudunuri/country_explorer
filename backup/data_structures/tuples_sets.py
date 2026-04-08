
VALID_REGIONS = (
    "Africa", "Americas", "Asia",
    "Europe", "Oceania", "Antarctic"
)

region = input("Enter the region: ").strip()
if region in VALID_REGIONS:
    print(f" Valid region: {region}")

else:
    print(f" Valid option: {', '.join (VALID_REGIONS)}")

searched = set()

searched.add("Japan")
searched.add("Germany")
searched.add("Japan")
searched.add("Brazil")

print(f" Unique Countries {len(searched)}")
print(searched)
