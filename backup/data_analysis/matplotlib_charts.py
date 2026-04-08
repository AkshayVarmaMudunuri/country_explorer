import matplotlib.pyplot as plt

names  = ["Germany", "France", "Poland", "Greece"]
pops   = [83200000, 67400000, 38000000, 10700000]

pop_m = [p/ 1_000_000 for p in pops]

plt.figure(figsize = (10,5))
bars = plt.bar(names, pop_m, color="#F03612")
plt.title(" Population by countries (Millions) ")
plt.ylabel(" Population in Millions ")
plt.xlabel(" Country ")

for bar, val in zip(bars, pop_m):
    plt.text(bar.get_x() + bar.get_width()/2,
    bar.get_height() + 0.5,
    f"{val:.1f}M", ha="center")

plt.tight_layout()
plt.savefig("reports/population_chart.png", dpi=150)
plt.show()
print("Chart saved to reports/population_chart.png")
