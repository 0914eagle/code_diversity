
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_map_size(polygon_area, map_count):
    side_length = int(math.sqrt(polygon_area / map_count))
    return side_length

def get_map_count(polygon_area, side_length):
    map_count = int(polygon_area / (side_length * side_length))
    return map_count

def get_maps(vertices, map_count):
    polygon_area = get_polygon_area(vertices)
    side_length = get_map_size(polygon_area, map_count)
    map_count = get_map_count(polygon_area, side_length)

    maps = []
    for i in range(map_count):
        map_vertices = []
        for j in range(len(vertices)):
            x, y = vertices[j]
            if x >= 0 and y >= 0:
                map_vertices.append((x - i * side_length, y - i * side_length))
            elif x < 0 and y >= 0:
                map_vertices.append((x - (i+1) * side_length, y - i * side_length))
            elif x >= 0 and y < 0:
                map_vertices.append((x - i * side_length, y - (i+1) * side_length))
            else:
                map_vertices.append((x - (i+1) * side_length, y - (i+1) * side_length))
        maps.append(map_vertices)

    return maps

def main():
    n, k = map(int, input().split())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    maps = get_maps(vertices, k)
    print(f"{get_map_size(get_polygon_area(vertices), k):.2f}")

if __name__ == '__main__':
    main()

