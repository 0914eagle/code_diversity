
import math

def read_input():
    N = int(input())
    contours = []
    for _ in range(N):
        H_0, H_1, M = map(int, input().split())
        points = []
        for _ in range(M):
            x, y = map(int, input().split())
            points.append((x, y))
        contours.append((H_0, H_1, points))
    return contours

def get_closest_distance(contours):
    min_distance = float('inf')
    for H_0, H_1, points in contours:
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i+1)%len(points)]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            min_distance = min(min_distance, distance)
    return min_distance

def get_closest_slanted_distance(contours):
    min_distance = float('inf')
    for H_0, H_1, points in contours:
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i+1)%len(points)]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            slanted_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (H_1-H_0)**2)
            min_distance = min(min_distance, slanted_distance)
    return min_distance

def main():
    contours = read_input()
    print(get_closest_distance(contours))
    print(get_closest_slanted_distance(contours))

if __name__ == '__main__':
    main()

