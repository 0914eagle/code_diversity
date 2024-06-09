
import math

def convex_polygon_score(points):
    # Calculate the convex hull of the points
    hull = []
    points = sorted(points)
    for p in points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    for p in reversed(points):
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    hull.pop()

    # Calculate the number of points inside the convex hull
    inside_points = 0
    for p in points:
        if is_inside_convex_polygon(hull, p):
            inside_points += 1

    # Calculate the score
    score = 2 ** inside_points

    return score

def cross_product(p1, p2, q):
    return (p1[0] - q[0]) * (p2[1] - q[1]) - (p1[1] - q[1]) * (p2[0] - q[0])

def is_inside_convex_polygon(polygon, point):
    x, y = point
    inside = False
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if p1[1] <= y:
            if p2[1] > y:
                if cross_product(p1, p2, point) > 0:
                    inside = not inside
        elif p2[1] <= y:
            if cross_product(p1, p2, point) < 0:
                inside = not inside
    return inside

def main():
    points = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        points.append((x, y))
    print(convex_polygon_score(points) % 998244353)

if __name__ == "__main__":
    main()

