
import math

def get_polygon_area(polygon):
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % len(polygon)]
        area += x1*y2 - x2*y1
    return abs(area/2)

def get_map_area(map_size):
    return map_size**2

def get_map_scale(map_size, polygon_area):
    return math.sqrt(polygon_area / get_map_area(map_size))

def get_map_size(polygon, k):
    polygon_area = get_polygon_area(polygon)
    map_scale = get_map_scale(1, polygon_area)
    map_size = int(map_scale * math.sqrt(polygon_area / k))
    return map_size

def f1(n, k):
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    return get_map_size(polygon, k)

def f2(...):
    ...

if __name__ == '__main__':
    f1(4, 1)
    f2(...)

