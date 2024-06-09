
import math

def convex_polygon_score(points):
    # Find the convex hull of the points
    hull = []
    for p in points:
        if len(hull) == 0 or hull[-1] != p:
            hull.append(p)
    while len(hull) > 2:
        a, b, c = hull[-3:]
        if orientation(a, b, c) == 0:
            hull.pop()
        else:
            break
    hull.reverse()

    # Count the number of points inside the convex hull
    inside_count = 0
    for p in points:
        if is_inside_convex_polygon(p, hull):
            inside_count += 1

    # Calculate the score
    score = 2 ** inside_count

    return score

def orientation(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    if val == 0:
        return 0
    if val > 0:
        return 1
    return 2

def is_inside_convex_polygon(p, polygon):
    x, y = p
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if orientation(p1, p2, p) == 2:
            return False
    return True

def main():
    points = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        points.append((x, y))

    scores = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if orientation(points[i], points[j], points[k]) == 0:
                    continue
                score = convex_polygon_score([points[i], points[j], points[k]])
                scores.append(score)

    print(sum(scores) % 998244353)

if __name__ == "__main__":
    main()

