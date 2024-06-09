
import math

def count_good_lines(n, points):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def get_slope(x, y):
        if x == 0:
            return (0, 1)
        if y == 0:
            return (1, 0)
        g = gcd(abs(x), abs(y))
        return (x // g, y // g)

    def get_central_point(points):
        x_sum = sum(x for x, y in points)
        y_sum = sum(y for x, y in points)
        return (x_sum / n, y_sum / n)

    def is_symmetric(points, slope):
        central_x, central_y = get_central_point(points)
        for x, y in points:
            x_diff = x - central_x
            y_diff = y - central_y
            if (x_diff, y_diff) != (0, 0) and get_slope(x_diff, y_diff) != slope:
                return False
        return True

    if n == 1:
        return -1

    good_lines = set()
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            slope = get_slope(x2 - x1, y2 - y1)
            if slope not in good_lines and is_symmetric(points, slope):
                good_lines.add(slope)

    if len(good_lines) == 0:
        return -1
    else:
        return len(good_lines)

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = count_good_lines(n, points)
print(result)
