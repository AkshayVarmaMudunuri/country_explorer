import os 
from datetime import date

def save_report(country):
    os.makedirs("reports", exist_ok=True)

    today = date.today().strftime("%Y-%m-%d")
    safe_name = country["name"].replace(" ", "_")
    filename = f"reports/{safe_name}_{today}.txt"

    lines = [
        f"Country Explorer Report",
        f"Generated: {today}",
        f"{'=' * 40}",
        f"Country:    {country['name']}",
        f"Capital:    {country['capital']}",
        f"Population: {country['population']:,}",
        f"Region:     {country['region']}",
        f"Languages:  {', '.join(country['languages'])}",
        f"Currency:   {country['currency']}",
    ]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".json(lines))

    print(f"  Report saved: {filename}")