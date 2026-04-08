print("Country Explorer - type 'q' to quit")

while True:
    name = input("Enter the country name: ").strip()

    if name.lower() == "q":
        print("Good Bye!")
        break

    if not name:
        print("Please Type Country name:")
        continue

    print(f" looking up {name.title()}...")

