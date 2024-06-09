
n, m = map(int, input().split())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

points = set()
for i in range(1, m + 1):
    points.add(i)

for l, r in segments:
    for i in range(l, r + 1):
        points.remove(i)

print(len(points))
if points:
    print(*points)

