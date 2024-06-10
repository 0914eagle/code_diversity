
import math

def get_spring_and_town_coordinates(n, s, t, h):
    # Function to get the coordinates of the springs and towns
    spring_coordinates = []
    town_coordinates = []
    for i in range(s):
        spring_coordinates.append([int(x) for x in input().split()])
    for i in range(t):
        town_coordinates.append([int(x) for x in input().split()])
    return spring_coordinates, town_coordinates

def get_hill_coordinates(n):
    # Function to get the coordinates of the hills
    hill_coordinates = []
    for i in range(n):
        x, y, h = [int(x) for x in input().split()]
        hill_coordinates.append([x, y, h])
    return hill_coordinates

def find_shortest_path(start, end, hill_coordinates):
    # Function to find the shortest path between two points on a 2D grid
    queue = [(0, start)]
    visited = set()
    while queue:
        dist, curr = queue.pop(0)
        if curr == end:
            return dist
        for neighbor in [(curr[0] + 1, curr[1]), (curr[0] - 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1)]:
            if 0 <= neighbor[0] < len(hill_coordinates) and 0 <= neighbor[1] < len(hill_coordinates[0]) and neighbor not in visited and hill_coordinates[neighbor[0]][neighbor[1]] != 0:
                queue.append((dist + 1, neighbor))
                visited.add(neighbor)
    return -1

def solve(n, s, t, q):
    # Function to solve the problem
    spring_coordinates, town_coordinates = get_spring_and_town_coordinates(n, s, t, q)
    hill_coordinates = get_hill_coordinates(n)
    total_length = 0
    for i in range(t):
        spring_coordinate = spring_coordinates[i]
        town_coordinate = town_coordinates[i]
        shortest_path = find_shortest_path(spring_coordinate, town_coordinate, hill_coordinates)
        if shortest_path == -1:
            return "IMPOSSIBLE"
        total_length += shortest_path
    return total_length

if __name__ == '__main__':
    n, s, t, q = [int(x) for x in input().split()]
    print(solve(n, s, t, q))

