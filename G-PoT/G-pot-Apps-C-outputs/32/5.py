
n = int(input())
points = list(map(int, input().split()))

julia_points = points[0]
max_points = max(points)

matches = 0
while max_points > julia_points:
    matches += 1
    julia_points += 1

print(matches)
