
n = int(input())
points = list(map(int, input().split()))

julia_points = points[0]
max_points = max(points)

matches = 0
while julia_points <= max_points:
    matches += 1
    julia_points += 1
    max_points = max([p if p < julia_points else p-1 for p in points])

print(matches)
