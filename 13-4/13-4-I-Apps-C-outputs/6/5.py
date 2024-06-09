
import math

def get_expected_distance(n, points):
    # Calculate the area of the CBD polygon
    area = get_area(n, points)
    
    # Calculate the expected distance traveled by a taxi
    expected_distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        expected_distance += get_distance(x1, y1, x2, y2) * area / (2*math.pi)
    
    return expected_distance

def get_area(n, points):
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        area += x1*y2 - x2*y1
    return abs(area)/2

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_expected_distance(n, points))

if __name__ == '__main__':
    main()

