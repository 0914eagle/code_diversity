
import math

def expected_distance(n, points):
    total_distance = 0
    for i in range(n):
        point1, point2 = points[i], points[i-1]
        total_distance += math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return total_distance / n

