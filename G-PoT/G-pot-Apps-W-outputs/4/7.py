
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_good_lines(points):
    n = len(points)
    if n == 1:
        return -1

    good_lines = set()
    for i in range(n):
        slopes = defaultdict(int)
        same_points = 0
        for j in range(n):
            if i != j:
                x_diff = points[j][0] - points[i][0]
                y_diff = points[j][1] - points[i][1]
                if x_diff == 0 and y_diff == 0:
                    same_points += 1
                else:
                    common_divisor = gcd(abs(x_diff), abs(y_diff))
                    slope = (x_diff // common_divisor, y_diff // common_divisor)
                    slopes[slope] += 1

        max_count = max(slopes.values()) if slopes else 0
        good_lines.add((max_count + same_points, points[i]))

    if len(good_lines) == 1:
        return -1
    else:
        return len(good_lines)

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = count_good_lines(points)
print(result)
