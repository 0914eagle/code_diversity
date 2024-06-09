
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1)%len(vertices)]
        area += x1*y2 - x2*y1
    return abs(area)/2

def get_map_size(vertices, k):
    area = get_polygon_area(vertices)
    side_length = int(math.sqrt(area/k))
    return side_length

def f1(n, k):
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    return get_map_size(vertices, k)

def f2(n, k):
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    return get_map_size(vertices, k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))
    print(f2(n, k))

