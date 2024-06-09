
import math

def expected_distance(n, points):
    area = 0
    for i in range(n):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area = abs(area) / 2

    distance = 0
    for i in range(n):
        p1 = points[i]
        p2 = points[(i+1) % n]
        side = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        distance += side * (area / side)

    return distance

