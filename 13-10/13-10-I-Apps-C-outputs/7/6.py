
import math

def get_distance(point1, point2):
    return math.sqrt(sum([(p1 - p2) ** 2 for p1, p2 in zip(point1, point2)]))

def get_shortest_distance(planets, home_planet):
    distances = []
    for planet in planets:
        if planet == home_planet:
            continue
        distances.append(get_distance(planet, home_planet))
    return sum(distances)

def get_revisited_planets(planets, home_planet):
    revisited_planets = [home_planet]
    for planet in planets:
        if planet == home_planet:
            continue
        revisited_planets.append(planet)
    return revisited_planets

def get_minimum_distance(planets, home_planet):
    revisited_planets = get_revisited_planets(planets, home_planet)
    minimum_distance = float('inf')
    for i in range(len(revisited_planets)):
        for j in range(i, len(revisited_planets)):
            distance = get_distance(revisited_planets[i], revisited_planets[j])
            if distance < minimum_distance:
                minimum_distance = distance
    return minimum_distance + get_shortest_distance(planets, home_planet)

def main():
    num_planets = int(input())
    planets = []
    for _ in range(num_planets):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    home_planet = planets[0]
    print(get_minimum_distance(planets, home_planet))

if __name__ == '__main__':
    main()

