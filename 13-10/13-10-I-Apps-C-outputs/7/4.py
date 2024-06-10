
import math

def get_distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(3)]))

def get_portals(planets):
    portals = []
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            portals.append((planets[i], planets[j]))
    return portals

def get_shortest_distance(planets, portals):
    distances = []
    for i in range(len(planets)):
        distances.append(get_distance(planets[i], planets[0]))
    for portal in portals:
        distances.append(get_distance(portal[0], portal[1]))
    return min(distances)

def main():
    num_planets = int(input())
    planets = []
    for i in range(num_planets):
        planets.append([int(x) for x in input().split()])
    portals = get_portals(planets)
    print(get_shortest_distance(planets, portals))

if __name__ == '__main__':
    main()

