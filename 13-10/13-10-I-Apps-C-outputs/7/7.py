
import math

def get_dist(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(3)]))

def get_shortest_distance(planets, home_planet):
    # Initialize the distance matrix with the distances between all pairs of planets
    dist_matrix = [[get_dist(planets[i], planets[j]) for j in range(len(planets))] for i in range(len(planets))]
    
    # Initialize the visited matrix with False for all planets
    visited = [False] * len(planets)
    
    # Initialize the current planet as the home planet
    current_planet = home_planet
    
    # Initialize the total distance traveled as 0
    total_distance = 0
    
    # Loop through all planets
    for i in range(len(planets)):
        # If the current planet has not been visited, visit it and calculate the distance traveled
        if not visited[current_planet]:
            visited[current_planet] = True
            total_distance += dist_matrix[current_planet][home_planet]
            current_planet = home_planet
        # If the current planet has been visited, find the unvisited planet with the minimum distance and visit it
        else:
            min_dist = float('inf')
            for j in range(len(planets)):
                if not visited[j] and dist_matrix[current_planet][j] < min_dist:
                    min_dist = dist_matrix[current_planet][j]
                    next_planet = j
            visited[next_planet] = True
            total_distance += min_dist
            current_planet = next_planet
    
    return total_distance

def main():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append([x, y, z])
    home_planet = 0
    print(get_shortest_distance(planets, home_planet))

if __name__ == '__main__':
    main()

