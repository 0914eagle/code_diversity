
import math

def count_points(points, distance):
    count = 0
    for point in points:
        if math.sqrt(point[0]**2 + point[1]**2) <= distance:
            count += 1
    return count

points = []
distance = None

# Read input
N, distance = map(int, input().split())
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# Count points within distance
result = count_points(points, distance)

# Print result
print(result)

