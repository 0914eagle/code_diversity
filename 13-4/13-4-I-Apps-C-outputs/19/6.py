
import math

def get_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_vertices(vertices, x_a, y_a, x_b, y_b):
    symmetric_vertices = []
    for i in range(len(vertices)):
        x, y = vertices[i]
        symmetric_vertices.append((x_b - x_a + x, y_b - y_a + y))
    return symmetric_vertices

def get_largest_corn_area(vertices, x_a, y_a, x_b, y_b):
    symmetric_vertices = get_symmetric_vertices(vertices, x_a, y_a, x_b, y_b)
    largest_area = 0
    for i in range(len(symmetric_vertices)):
        area = get_area(symmetric_vertices[i:i+3])
        if area > largest_area:
            largest_area = area
    return largest_area

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

