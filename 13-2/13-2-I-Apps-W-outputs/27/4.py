
import sys

n = int(input().strip())
points = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    points.append((x, y))

max_distance = 0
for i in range(n):
    for j in range(i+1, n):
        distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        max_distance = max(max_distance, distance)

print(max_distance)

