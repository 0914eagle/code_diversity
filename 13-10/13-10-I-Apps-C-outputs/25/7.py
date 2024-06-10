
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_polygon_centroid(vertices):
    area = get_polygon_area(vertices)
    cx = cy = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        cross = x1 * y2 - x2 * y1
        cx += (x1 + x2) * cross
        cy += (y1 + y2) * cross
    cx /= 6 * area
    cy /= 6 * area
    return cx, cy

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_cut_cost(vertices, centroid):
    cost = 0
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)]
        cost += get_distance(v1, centroid) + get_distance(v2, centroid)
    return cost

def get_min_cut_cost(vertices, hole_vertices):
    min_cost = float('inf')
    for i in range(len(hole_vertices)):
        v1 = hole_vertices[i]
        v2 = hole_vertices[(i + 1) % len(hole_vertices)]
        line_centroid = (v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2
        cost = get_cut_cost(vertices, line_centroid)
        if cost < min_cost:
            min_cost = cost
    return min_cost

def main():
    num_vertices = int(input())
    vertices = []
    for i in range(num_vertices):
        x, y = map(int, input().split())
        vertices.append((x, y))
    num_hole_vertices = int(input())
    hole_vertices = []
    for i in range(num_hole_vertices):
        x, y = map(int, input().split())
        hole_vertices.append((x, y))
    cost = get_min_cut_cost(vertices, hole_vertices)
    print(cost)

if __name__ == '__main__':
    main()

