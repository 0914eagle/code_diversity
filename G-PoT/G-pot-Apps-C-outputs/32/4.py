
n = int(input())
points = list(map(int, input().split()))

julia_points = points[0]
max_other_points = max(points[1:])

matches = 0
while julia_points <= max_other_points:
    matches += 1
    julia_points += 1
    max_other_points = max([p-1 for p in points[1:]])

print(matches)
