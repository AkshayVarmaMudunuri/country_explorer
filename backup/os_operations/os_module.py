import os

if os.path.exists("data/cache.json"):
    print("Cache file found")

else:
    print("No cache yet")

os.makedirs("data", exist_ok= True)
os.makedirs("reports", exist_ok=True)

filename = os.path.join("reports", "japan_report.txt")
print(filename)