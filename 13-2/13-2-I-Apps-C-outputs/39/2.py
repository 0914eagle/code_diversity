
import math

def convex_polygon_score(points):
    # Find the convex hull of the points
    hull = []
    for p in points:
        if len(hull) == 0 or hull[-1] != p:
            hull.append(p)
    while len(hull) > 2:
        a, b, c = hull[-3:]
        if ccw(a, b, c) == 0:
            hull.pop()
        else:
            break
    hull.reverse()

    # Count the number of points inside the convex hull
    inside_count = 0
    for p in points:
        if ccw(hull[0], hull[1], p) >= 0 and ccw(hull[-2], hull[-1], p) >= 0:
            inside_count += 1

    # Calculate the score
    score = 2 ** (inside_count - len(hull))

    return score

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def solve(points):
    scores = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if ccw(points[i], points[j], points[k]) == 0:
                    continue
                score = convex_polygon_score([points[i], points[j], points[k]])
                scores.append(score)
    return sum(scores) % 998244353

points = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))
print(solve(points))

