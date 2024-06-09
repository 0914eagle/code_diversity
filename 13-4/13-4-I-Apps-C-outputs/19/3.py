
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b):
    # Find the midpoint of the line segment representing the canal
    x_m = (x_a + x_b) / 2
    y_m = (y_a + y_b) / 2
    
    # Find the reflection of the polygon about the midpoint
    reflected_vertices = []
    for vertex in vertices:
        x, y = vertex
        reflected_vertices.append((x_m * 2 - x, y_m * 2 - y))
    
    # Find the area of the original polygon and its reflection about the midpoint
    original_area = get_polygon_area(vertices)
    reflected_area = get_polygon_area(reflected_vertices)
    
    # Return the difference between the two areas
    return original_area - reflected_area

def main():
    N = int(input())
    vertices = []
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b))

if __name__ == '__main__':
    main()

