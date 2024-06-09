
import sys

N, M = map(int, input().split())
cities = []

for i in range(M):
    P, Y = map(int, input().split())
    cities.append((P, Y))

cities.sort(key=lambda x: (x[0], x[1]))

for city in cities:
    print(f"{city[0]:06}{city[1]:06}")

