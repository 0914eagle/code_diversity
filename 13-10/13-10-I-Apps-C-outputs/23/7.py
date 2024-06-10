
import sys
import math

def get_input():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    return n, planets

def tunnel_cost(planet1, planet2):
    return abs(planet1[0] - planet2[0]) + abs(planet1[1] - planet2[1]) + abs(planet1[2] - planet2[2])

def get_min_cost(n, planets):
    cost = 0
    for i in range(n):
        for j in range(i+1, n):
            cost += tunnel_cost(planets[i], planets[j])
    return cost

def main():
    n, planets = get_input()
    print(get_min_cost(n, planets))

if __name__ == '__main__':
    main()

