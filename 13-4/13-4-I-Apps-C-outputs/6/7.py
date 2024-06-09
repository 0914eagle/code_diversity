
import math

def get_expected_distance(n, points):
    total_distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        total_distance += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return total_distance / n

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_expected_distance(n, points))

if __name__ == '__main__':
    main()

