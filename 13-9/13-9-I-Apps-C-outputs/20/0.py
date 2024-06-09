
import math

def expected_distance(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[(i+1)%n][1] - points[i][1] * points[(i+1)%n][0]
    area = abs(area) / 2

    # Calculate the expected distance traveled by the taxi
    dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist += abs(dx+dy) * area / n

    return dist

