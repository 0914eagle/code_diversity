
import math

def get_distance(x, y):
    return math.sqrt(x**2 + y**2)

def get_min_distance(points):
    min_distance = float('inf')
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            distance = get_distance(points[i][0] - points[j][0], points[i][1] - points[j][1])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_slanted_distance(points):
    min_distance = get_min_distance(points)
    return min_distance / math.sqrt(2)

def main():
    num_contours = int(input())
    points = []
    for _ in range(num_contours):
        outer_height, inner_height, num_vertices = map(int, input().split())
        for _ in range(num_vertices):
            x, y = map(int, input().split())
            points.append((x, y))
    print(get_slanted_distance(points))

if __name__ == '__main__':
    main()

