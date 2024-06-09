
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

def minimum_spanning_tree(points):
    tree = []
    visited = set()
    while points:
        min_dist = float('inf')
        min_point = None
        for point in points:
            if point not in visited:
                dist = manhattan_distance(point, min_point) if min_point else 0
                if dist < min_dist:
                    min_dist = dist
                    min_point = point
        tree.append((min_point, min_dist))
        visited.add(min_point)
        points.remove(min_point)
    return tree

def main():
    points = get_points(input)
    tree = minimum_spanning_tree(points)
    print(sum(dist for _, dist in tree))

if __name__ == '__main__':
    main()

