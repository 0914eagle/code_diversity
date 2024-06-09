
import math

def get_distance(x1, y1, x2, y2):
    return math.fabs(x1 - x2) + math.fabs(y1 - y2)

def get_expected_distance(n, points):
    total_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            total_distance += get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
    return total_distance / (n * (n - 1))

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_expected_distance(n, points))

if __name__ == '__main__':
    main()

