
import math

def get_polygon_area(vertices):
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1) % len(vertices)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b):
    # Find the center of the polygon
    x_center = (x_a + x_b) / 2
    y_center = (y_a + y_b) / 2
    
    # Translate the polygon to the origin
    translated_vertices = [(x - x_center, y - y_center) for x, y in vertices]
    
    # Rotate the polygon by 180 degrees
    rotated_vertices = [(x, -y) for x, y in translated_vertices]
    
    # Find the area of the rotated polygon
    area = get_polygon_area(rotated_vertices)
    
    # Return the area of the symmetric polygon
    return area

def get_max_corn_area(vertices, x_a, y_a, x_b, y_b):
    # Find the area of the symmetric polygon
    symmetric_area = get_symmetric_polygon_area(vertices, x_a, y_a, x_b, y_b)
    
    # Find the area of the original polygon
    original_area = get_polygon_area(vertices)
    
    # Return the maximum area
    return max(symmetric_area, original_area)

def main():
    # Read the input
    N = int(input())
    vertices = []
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x_a, y_a, x_b, y_b = map(int, input().split())
    
    # Find the maximum area
    max_area = get_max_corn_area(vertices, x_a, y_a, x_b, y_b)
    
    # Print the result
    print(max_area)

if __name__ == '__main__':
    main()

