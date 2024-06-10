
import math

def get_distance(planet1, planet2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(planet1, planet2)]))

def get_shortest_distance(planets, home_planet):
    distances = []
    for planet in planets:
        if planet == home_planet:
            continue
        distances.append(get_distance(home_planet, planet))
    return sum(distances)

def get_shortest_distance_with_portals(planets, home_planet):
    distances = []
    for planet in planets:
        if planet == home_planet:
            continue
        distances.append(get_distance(home_planet, planet))
    return sum(distances)

if __name__ == '__main__':
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        planet = tuple(map(int, input().split()))
        planets.append(planet)
    home_planet = planets[0]
    print(get_shortest_distance(planets, home_planet))
    print(get_shortest_distance_with_portals(planets, home_planet))

