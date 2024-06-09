
n, m = map(int, input().split())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append([l, r])

points = set()

for segment in segments:
    for i in range(segment[0], segment[1] + 1):
        points.add(i)

non_segment_points = set(range(1, m + 1)) - points

print(len(non_segment_points))

if len(non_segment_points) == 0:
    print(0)
else:
    print(*non_segment_points)

