
import math

def solve(n, points):
    # Calculate the area of the CBD polygon
    area = 0
    for i in range(n):
        area += points[i][0] * points[i-1][1] - points[i-1][0] * points[i][1]
    area = abs(area) / 2

    # Calculate the distance of the taxi traveling between the points
    distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        distance += math.sqrt((x2-x1)**2 + (y2-y1)**2)

    # Calculate the expected distance
    expected_distance = distance * area / n

    return expected_distance

