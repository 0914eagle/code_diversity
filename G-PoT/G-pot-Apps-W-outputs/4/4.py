
import math

def count_good_lines(n, points):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def get_slope(x, y):
        g = gcd(abs(x), abs(y))
        return (x // g, y // g)

    def get_central_point(x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def is_good_line(slope, central_point):
        symmetric_points = set()
        for x, y in points:
            dx = x - central_point[0]
            dy = y - central_point[1]
            if dx == 0 and dy == 0:
                continue
            current_slope = get_slope(dx, dy)
            if current_slope != slope:
                symmetric_points.add(current_slope)
        return len(symmetric_points) == 0

    good_lines = set()
    for i in range(n):
        for j in range(i + 1, n):
            slope = get_slope(points[j][0] - points[i][0], points[j][1] - points[i][1])
            central_point = get_central_point(points[i][0], points[i][1], points[j][0], points[j][1])
            if is_good_line(slope, central_point):
                good_lines.add((slope, central_point))

    if len(good_lines) == 0:
        return -1
    return len(good_lines)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
result = count_good_lines(n, points)
print(result)
