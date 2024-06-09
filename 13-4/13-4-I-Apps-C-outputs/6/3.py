
import math

def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_expected_distance(points):
    total_distance = 0
    for i in range(len(points)):
        point1 = points[i]
        point2 = points[(i+1) % len(points)]
        total_distance += get_distance(point1, point2)
    return total_distance / len(points)

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_expected_distance(points))

if __name__ == '__main__':
    main()

