
import sys

n, m = map(int, input().split())
cities = []

for i in range(m):
    p, y = map(int, input().split())
    cities.append((p, y))

cities.sort(key=lambda x: (x[0], x[1]))

for city in cities:
    print(f"{city[0]:0>6}{city[1]:0>6}")

