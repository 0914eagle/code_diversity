
import math

def get_new_coordinates(coordinates, area):
    # Calculate the current area of the polygon
    current_area = get_polygon_area(coordinates)
    
    # Calculate the ratio of the current area to the desired area
    area_ratio = area / current_area
    
    # Calculate the new coordinates of the polygon
    new_coordinates = []
    for x, y in coordinates:
        new_x = x * area_ratio
        new_y = y * area_ratio
        new_coordinates.append((new_x, new_y))
    
    return new_coordinates

def get_polygon_area(coordinates):
    area = 0
    for i in range(len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % len(coordinates)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def main():
    coordinates = [(0, 0), (1, 1), (0, 2)]
    area = 4
    new_coordinates = get_new_coordinates(coordinates, area)
    print(new_coordinates)

if __name__ == '__main__':
    main()

