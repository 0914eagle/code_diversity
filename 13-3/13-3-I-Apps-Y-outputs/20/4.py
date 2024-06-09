
import sys

n, m = map(int, input().split())
cities = []

for i in range(m):
    p, y = map(int, input().split())
    cities.append((p, y))

cities.sort(key=lambda x: (x[0], x[1]))

for city in cities:
    print("{:0>6}{:0>6}".format(city[0], city[1]))

