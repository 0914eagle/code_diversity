
import math

def get_input():
    N = int(input())
    polygon = []
    for i in range(N):
        x, y = map(float, input().split())
        polygon.append((x, y))
    A = int(input())
    return polygon, A

def resize_polygon(polygon, A):
    # Calculate the area of the original polygon
    area = get_area(polygon)
    
    # Calculate the ratio of the new area to the original area
    ratio = A / area
    
    # Resize the polygon by scaling each vertex by the ratio
    resized_polygon = [(x * ratio, y * ratio) for x, y in polygon]
    
    # Return the resized polygon
    return resized_polygon

def get_area(polygon):
    # Calculate the area of the polygon by taking the absolute value of the
    # cross product of two consecutive vertices
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        area += abs(x1 * y2 - x2 * y1)
    
    # Return the area
    return area / 2

def main():
    polygon, A = get_input()
    resized_polygon = resize_polygon(polygon, A)
    for x, y in resized_polygon:
        print(f"{x:.4f} {y:.4f}")

if __name__ == '__main__':
    main()

