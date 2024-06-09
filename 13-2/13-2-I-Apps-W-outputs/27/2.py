
import sys

n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        max_dist = max(max_dist, dist)

print(max_dist)

