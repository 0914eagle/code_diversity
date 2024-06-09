
n = int(input())
points = list(map(int, input().split()))

julia_points = points[0]
max_points = max(points)

if points.count(max_points) == 1:
    print(0)
else:
    diff = max_points - julia_points
    if diff == 0:
        print(1)
    else:
        print(diff)
