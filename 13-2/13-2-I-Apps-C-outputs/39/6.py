
import math

def convex_polygon_score(points):
    # Find the convex hull of the points
    hull = []
    for p in points:
        if len(hull) == 0 or hull[-1] != p:
            hull.append(p)
    while len(hull) > 2 and hull[-2] == hull[0]:
        hull.pop()
    if len(hull) <= 2:
        return 0
    
    # Calculate the area of the polygon
    area = 0
    for i in range(len(hull)):
        p1 = hull[i]
        p2 = hull[(i+1) % len(hull)]
        area += p1[0] * p2[1] - p1[1] * p2[0]
    area = abs(area) / 2
    
    # Calculate the number of points inside the convex hull
    inside_points = 0
    for p in points:
        if p in hull:
            continue
        inside = False
        for i in range(len(hull)):
            p1 = hull[i]
            p2 = hull[(i+1) % len(hull)]
            if (p1[1] > p[1]) != (p2[1] > p[1]) and p[0] < (p2[0] - p1[0]) * (p[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
                inside = not inside
        if inside:
            inside_points += 1
    
    # Calculate the score
    score = math.pow(2, inside_points - len(hull))
    
    return score

def solve(points):
    scores = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if points[i] == points[j] or points[j] == points[k] or points[k] == points[i]:
                    continue
                score = convex_polygon_score([points[i], points[j], points[k]])
                if score > 0:
                    scores.append(score)
    
    return sum(scores) % 998244353

points = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))

print(solve(points))

