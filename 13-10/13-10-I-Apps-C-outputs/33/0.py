
def read_points():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def count_sets(points, l, r, a):
    sets = set()
    for x, y in points:
        if l < x < r and y > a:
            sets.add((x, y))
    return len(sets)

def solve(points):
    l = min(point[0] for point in points)
    r = max(point[0] for point in points)
    a = max(point[1] for point in points)
    return count_sets(points, l, r, a)

if __name__ == '__main__':
    points = read_points()
    print(solve(points))

