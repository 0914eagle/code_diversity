
import math

def get_expected_distance(n, points):
    total_distance = 0
    for i in range(n):
        point1 = points[i]
        point2 = points[(i+1)%n]
        total_distance += math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
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

