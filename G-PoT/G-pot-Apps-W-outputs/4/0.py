
import math

def count_good_lines(points):
    def get_slope(point):
        x, y = point
        if x == 0:
            return float('inf')
        return y / x

    def get_distance(point):
        x, y = point
        return math.sqrt(x**2 + y**2)

    slopes = set()
    distances = set()

    for point in points:
        slopes.add(get_slope(point))
        distances.add(get_distance(point))

    if len(slopes) == 1 or len(distances) == 1:
        return -1

    return len(points)

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = count_good_lines(points)
print(result)
