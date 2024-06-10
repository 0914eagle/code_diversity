
import math

def get_distance(planet1, planet2):
    return math.sqrt(sum([(p1 - p2) ** 2 for p1, p2 in zip(planet1, planet2)]))

def get_total_distance(planets, home_planet):
    total_distance = 0
    for planet in planets:
        if planet != home_planet:
            total_distance += get_distance(planet, home_planet)
    return total_distance

def get_shortest_distance(planets, home_planet):
    shortest_distance = math.inf
    for planet in planets:
        if planet != home_planet:
            distance = get_distance(planet, home_planet)
            if distance < shortest_distance:
                shortest_distance = distance
    return shortest_distance

def main():
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    home_planet = planets[0]
    planets.remove(home_planet)
    total_distance = get_total_distance(planets, home_planet)
    shortest_distance = get_shortest_distance(planets, home_planet)
    print(total_distance - shortest_distance)

if __name__ == '__main__':
    main()

