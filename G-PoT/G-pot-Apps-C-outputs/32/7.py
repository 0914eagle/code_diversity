
n = int(input())
points = list(map(int, input().split()))

max_points = max(points)
count = 0

for p in points:
    if p == max_points:
        count += 1

print(count)
