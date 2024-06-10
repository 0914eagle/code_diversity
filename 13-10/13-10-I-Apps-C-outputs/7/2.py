
import math

def get_distance(planet_1, planet_2):
    return math.sqrt(sum((x1 - x2)**2 for x1, x2 in zip(planet_1, planet_2)))

def get_min_distance(planets):
    home_planet = planets[0]
    visited_planets = [home_planet]
    total_distance = 0
    for planet in planets[1:]:
        if planet not in visited_planets:
            visited_planets.append(planet)
            total_distance += get_distance(planet, home_planet)
    return total_distance

def main():
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        planets.append(tuple(map(int, input().split())))
    print(get_min_distance(planets))

if __name__ == '__main__':
    main()

