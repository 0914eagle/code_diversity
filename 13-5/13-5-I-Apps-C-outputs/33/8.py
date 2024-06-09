
import math

def get_side_length(n, k):
    
    # Calculate the total area of the canyon
    total_area = get_total_area(n)

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = math.sqrt(map_area)

    return side_length

def get_total_area(n):
    
    # Calculate the area of each triangle
    triangle_area = 0
    for i in range(n):
        triangle_area += get_triangle_area(i, n)

    return triangle_area

def get_triangle_area(i, n):
    
    # Get the coordinates of the triangle
    x1, y1 = get_coordinates(i, n)
    x2, y2 = get_coordinates((i + 1) % n, n)
    x3, y3 = get_coordinates((i + 2) % n, n)

    # Calculate the area of the triangle
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    return area

def get_coordinates(i, n):
    
    # Read the coordinates from input
    x, y = map(int, input().split())

    return x, y

if __name__ == '__main__':
    # Read the number of vertices and maps from input
    n, k = map(int, input().split())

    # Calculate the side length of each map
    side_length = get_side_length(n, k)

    # Print the result
    print(f"{side_length:.2f}")

