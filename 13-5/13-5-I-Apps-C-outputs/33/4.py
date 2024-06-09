
import math

def get_canyon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1)%len(vertices)]
        area += x1*y2 - x2*y1
    return abs(area/2)

def get_map_side_length(canyon_area, map_count):
    side_length = math.sqrt(canyon_area / map_count)
    return round(side_length, 2)

def get_map_coordinates(canyon_vertices, map_count, map_index):
    canyon_area = get_canyon_area(canyon_vertices)
    map_side_length = get_map_side_length(canyon_area, map_count)
    map_width = map_side_length
    map_height = map_side_length
    map_x = map_index % map_count
    map_y = map_index // map_count
    map_left = map_x * map_width
    map_top = map_y * map_height
    map_right = map_left + map_width
    map_bottom = map_top + map_height
    return map_left, map_top, map_right, map_bottom

def f1(n, k):
    canyon_vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        canyon_vertices.append((x, y))
    return get_map_side_length(get_canyon_area(canyon_vertices), k)

def f2(n, k):
    canyon_vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        canyon_vertices.append((x, y))
    map_coordinates = []
    for i in range(k):
        map_left, map_top, map_right, map_bottom = get_map_coordinates(canyon_vertices, k, i)
        map_coordinates.append((map_left, map_top, map_right, map_bottom))
    return map_coordinates

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(f1(n, k))
    print(f2(n, k))

