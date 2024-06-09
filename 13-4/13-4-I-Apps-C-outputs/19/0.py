
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_area(vertices, x_a, y_a, x_b, y_b):
    area = 0
    for i in range(len(vertices)):
        x, y = vertices[i]
        if x >= x_a and x <= x_b and y >= y_a and y <= y_b:
            area += x * y_b - x_b * y
    return abs(area) / 2

def get_largest_corn_area(vertices, x_a, y_a, x_b, y_b):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        if x1 >= x_a and x1 <= x_b and y1 >= y_a and y1 <= y_b:
            area = max(area, get_symmetric_area(vertices, x1, y1, x2, y2))
    return area

def main():
    N = int(input())
    vertices = []
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(get_largest_corn_area(vertices, x_a, y_a, x_b, y_b))

if __name__ == '__main__':
    main()

