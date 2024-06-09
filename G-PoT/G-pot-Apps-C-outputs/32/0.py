
n = int(input())
points = list(map(int, input().split()))

julia_points = points[0]
max_points = max(points)

if points.count(max_points) == 1:
    print(0)
else:
    count = 0
    for i in range(1, n):
        if points[i] == max_points:
            count += 1
    print(max_points - julia_points + 1 - count)
