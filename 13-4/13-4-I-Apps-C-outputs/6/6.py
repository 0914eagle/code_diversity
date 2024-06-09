
import math

def get_expected_distance(n, points):
    # Calculate the area of the CBD polygon
    area = get_area(n, points)
    
    # Calculate the expected distance traveled by a taxi
    expected_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            expected_distance += get_distance(points[i], points[j])
    expected_distance /= n * (n-1)
    
    # Convert the expected distance to the expected distance traveled by a taxi within the CBD
    expected_distance *= area / get_area(n, points)
    
    return expected_distance

def get_area(n, points):
    area = 0
    for i in range(n):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    return abs(area) / 2

def get_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_expected_distance(n, points))

