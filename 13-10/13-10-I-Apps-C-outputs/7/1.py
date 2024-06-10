
import math

def get_distances(planets):
    distances = []
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            distance = math.sqrt(sum((planets[i] - planets[j])**2))
            distances.append(distance)
    return distances

def get_optimal_path(planets):
    distances = get_distances(planets)
    optimal_path = []
    visited = set()
    current_planet = 0
    while len(visited) < len(planets):
        next_planet = None
        minimum_distance = float('inf')
        for planet in range(len(planets)):
            if planet not in visited:
                distance = distances[current_planet * len(planets) + planet]
                if distance < minimum_distance:
                    minimum_distance = distance
                    next_planet = planet
        optimal_path.append(next_planet)
        visited.add(next_planet)
        current_planet = next_planet
    return optimal_path

def get_total_distance(planets, optimal_path):
    total_distance = 0
    for i in range(len(optimal_path) - 1):
        planet1 = planets[optimal_path[i]]
        planet2 = planets[optimal_path[i + 1]]
        total_distance += math.sqrt(sum((planet1 - planet2)**2))
    return total_distance

def main():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append([x, y, z])
    optimal_path = get_optimal_path(planets)
    total_distance = get_total_distance(planets, optimal_path)
    print(total_distance)

if __name__ == '__main__':
    main()

