
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b):
    symmetric_vertices = []
    for x, y in vertices:
        symmetric_vertices.append((x_b - x, y_b - y))
    return get_polygon_area(symmetric_vertices)

def get_max_corn_area(vertices, x_a, y_a, x_b, y_b):
    max_area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        if x1 == x2 and y1 == y2:
            continue
        area = get_symmetric_polygon_area(vertices[i:i+2], x_a, y_a, x_b, y_b)
        if area > max_area:
            max_area = area
    return max_area

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(get_max_corn_area(vertices, x_a, y_a, x_b, y_b))

if __name__ == '__main__':
    main()

