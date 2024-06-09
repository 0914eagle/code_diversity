
import math

def get_area(x1, y1, x2, y2, x3, y3):
    
    return math.fabs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def get_symmetric_points(x, y, x_a, y_a, x_b, y_b):
    
    m = (y_a - y_b) / (x_a - x_b)
    c = y_a - m * x_a
    x_sym = (x * m - y + c) / (m * m + 1)
    y_sym = m * x_sym + c
    return x_sym, y_sym

def get_largest_corn_area(vertices, x_a, y_a, x_b, y_b):
    
    # Get the symmetric points of the vertices about the line passing through (x_a, y_a) and (x_b, y_b)
    sym_vertices = [(get_symmetric_points(x, y, x_a, y_a, x_b, y_b)) for x, y in vertices]
    
    # Calculate the area of the triangle formed by the symmetric points
    areas = [get_area(x1, y1, x2, y2, x3, y3) for ((x1, y1), (x2, y2), (x3, y3)) in zip(sym_vertices, sym_vertices[1:], sym_vertices[2:])]
    
    # Return the largest area
    return max(areas)

def main():
    # Read the input
    n = int(input())
    vertices = [(int(x), int(y)) for x, y in [input().split() for _ in range(n)]]
    x_a, y_a, x_b, y_b = [int(x) for x in input().split()]
    
    # Calculate the largest possible area of land to grow corn fields for Alob
    area = get_largest_corn_area(vertices, x_a, y_a, x_b, y_b)
    
    # Print the output
    print(area)

if __name__ == '__main__':
    main()

