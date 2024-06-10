
import math

def get_dist(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def get_min_dist(planets, home_planet):
    visited = set([home_planet])
    total_dist = 0
    while len(visited) < len(planets):
        min_dist = float('inf')
        min_planet = None
        for planet in planets:
            if planet in visited:
                continue
            dist = get_dist(planet, home_planet)
            if dist < min_dist:
                min_dist = dist
                min_planet = planet
        visited.add(min_planet)
        total_dist += min_dist
        home_planet = min_planet
    return total_dist

def main():
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        planets.append(tuple(map(int, input().split())))
    print(get_min_dist(planets, planets[0]))

if __name__ == '__main__':
    main()

