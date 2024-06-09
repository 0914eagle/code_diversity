
import math

def get_input():
    N = int(input())
    polygon = []
    for i in range(N):
        x, y = map(float, input().split())
        polygon.append((x, y))
    A = int(input())
    return polygon, A

def get_new_polygon(polygon, A):
    # Calculate the area of the original polygon
    area = get_area(polygon)
    
    # Calculate the ratio of the new area to the original area
    ratio = A / area
    
    # Create a new polygon with the same number of corners as the original polygon
    new_polygon = [(0, 0)] * len(polygon)
    
    # Iterate through the corners of the original polygon
    for i, (x, y) in enumerate(polygon):
        # Calculate the new x and y coordinates for the corner
        new_x = x * ratio
        new_y = y * ratio
        
        # Add the new coordinates to the new polygon
        new_polygon[i] = (new_x, new_y)
    
    return new_polygon

def get_area(polygon):
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def main():
    polygon, A = get_input()
    new_polygon = get_new_polygon(polygon, A)
    for x, y in new_polygon:
        print(f"{x:.4f} {y:.4f}")

if __name__ == '__main__':
    main()

