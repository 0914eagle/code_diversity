
import sys
input = sys.stdin.read()

def get_points(input):
    N = int(input.split('\n')[0])
    points = []
    for i in range(1, N+1):
        x, y = map(int, input.split('\n')[i].split())
        points.append((x, y))
    return points

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def prims_algorithm(points):
    tree = []
    visited = set()
    current = points[0]
    visited.add(current)
    while len(visited) < len(points):
        min_distance = float('inf')
        for point in points:
            if point in visited:
                continue
            distance = manhattan_distance(current, point)
            if distance < min_distance:
                min_distance = distance
                current = point
        tree.append((current, manhattan_distance(current, points[0])))
        visited.add(current)
    return tree

def minimum_spanning_tree(points):
    tree = prims_algorithm(points)
    return sum(distance for _, distance in tree)

if __name__ == '__main__':
    points = get_points(input)
    print(minimum_spanning_tree(points))

