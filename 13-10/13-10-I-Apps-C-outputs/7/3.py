
import sys
import math

def get_distance(p1, p2):
    return math.sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2)))

def get_portal_distances(planets, portals):
    distances = []
    for i in range(len(planets)):
        for j in range(i, len(planets)):
            if i != j:
                distances.append((get_distance(planets[i], portals[i]), get_distance(planets[j], portals[j])))
    return distances

def get_optimal_journey(planets, portals):
    distances = get_portal_distances(planets, portals)
    distances.sort(key=lambda x: x[0] + x[1])
    journey = []
    for i in range(len(planets)):
        journey.append((distances[i][0], distances[i][1]))
    return journey

def get_total_distance(journey, planets):
    total_distance = 0
    for i in range(len(journey)):
        total_distance += journey[i][0] + journey[i][1]
    return total_distance

def main():
    num_planets = int(input())
    planets = []
    for i in range(num_planets):
        planets.append(tuple(map(int, input().split())))
    portals = [planets[0]]
    for i in range(1, num_planets):
        portals.append(tuple(map(int, input().split())))
    journey = get_optimal_journey(planets, portals)
    total_distance = get_total_distance(journey, planets)
    print(total_distance)

if __name__ == '__main__':
    main()

