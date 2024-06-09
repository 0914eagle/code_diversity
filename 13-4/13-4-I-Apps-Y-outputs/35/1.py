
n, m = map(int, input().split())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

points = set()

for i in range(1, m + 1):
    point_belongs_to_segment = False
    for l, r in segments:
        if l <= i <= r:
            point_belongs_to_segment = True
            break
    if not point_belongs_to_segment:
        points.add(i)

print(len(points))
if points:
    print(*points)

