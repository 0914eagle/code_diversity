
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        if x1 == x2:
            continue
        if x1 < x_a:
            x1 = x_a - (x_a - x1)
        if x2 < x_a:
            x2 = x_a - (x_a - x2)
        if x1 > x_b:
            x1 = x_b + (x1 - x_b)
        if x2 > x_b:
            x2 = x_b + (x2 - x_b)
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_max_corn_area(vertices, x_a, y_a, x_b, y_b):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        if x1 == x2:
            continue
        if x1 < x_a:
            x1 = x_a - (x_a - x1)
        if x2 < x_a:
            x2 = x_a - (x_a - x2)
        if x1 > x_b:
            x1 = x_b + (x1 - x_b)
        if x2 > x_b:
            x2 = x_b + (x2 - x_b)
        area = max(area, get_symmetric_polygon_area(vertices, x1, y1, x2, y2))
    return area

def main():
    vertices = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(get_max_corn_area(vertices, x_a, y_a, x_b, y_b))

if __name__ == '__main__':
    main()

