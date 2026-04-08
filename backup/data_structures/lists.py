
history = []

history.append("Japan")
history.append("Germany")
history.append("Brazil")

print(f"You searched {len(history)} countries:")

for i, country in enumerate(history,1):
    print(f" {i}. {country}")

print(f"First Search:  {history[0]}")
print(f"Last Search:   {history[-1]}")

if "Japan" in history:
    print("Japan is in your history")