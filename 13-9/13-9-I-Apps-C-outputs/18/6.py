
import math

def get_toys_coordinates(n):
    toys_coordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        toys_coordinates.append((x, y))
    return toys_coordinates

def get_trees_coordinates(m):
    trees_coordinates = []
    for i in range(m):
        x, y = map(int, input().split())
        trees_coordinates.append((x, y))
    return trees_coordinates

def find_shortest_path(start, end, toys_coordinates, trees_coordinates):
    visited = set()
    queue = [(0, start)]
    while queue:
        distance, current = queue.pop(0)
        if current == end:
            return distance
        if current in visited:
            continue
        visited.add(current)
        for toy in toys_coordinates:
            if toy not in visited and math.sqrt((current[0]-toy[0])**2 + (current[1]-toy[1])**2) <= 10000:
                queue.append((distance + 1, toy))
        for tree in trees_coordinates:
            if tree not in visited and math.sqrt((current[0]-tree[0])**2 + (current[1]-tree[1])**2) <= 10000:
                queue.append((distance + 1, tree))
    return -1

def main():
    n, m = map(int, input().split())
    toys_coordinates = get_toys_coordinates(n)
    trees_coordinates = get_trees_coordinates(m)
    shortest_path = find_shortest_path((0, 0), toys_coordinates[0], toys_coordinates, trees_coordinates)
    for i in range(1, n):
        shortest_path = min(shortest_path, find_shortest_path(toys_coordinates[i-1], toys_coordinates[i], toys_coordinates, trees_coordinates))
    print(f"{shortest_path:.2f}")

if __name__ == '__main__':
    main()

