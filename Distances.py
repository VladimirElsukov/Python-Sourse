import math
# Cловарь координат городов


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for city1, (x1, y1) in sites.items():
    distances[city1] = {}
    for city2, (x2, y2) in sites.items():
        if city1 != city2:
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            distances[city1][city2] = distance

# вывод
for city, dists in distances.items():
    print(f"{city}:")
    for dest_city, distance in dists.items():
        print(f"  - до {dest_city}: {distance:.2f}")
    print()  # Перенос строки между городами
