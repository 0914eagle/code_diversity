
import math

def get_min_circle_radius(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    x_mid = (x_min + x_max) / 2
    y_mid = (y_min + y_max) / 2
    x_diameter = x_max - x_min
    y_diameter = y_max - y_min
    radius = math.sqrt(x_diameter ** 2 + y_diameter ** 2) / 2
    return radius

def main():
    points = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        points.append((x, y))
    print(get_min_circle_radius(points))

if __name__ == '__main__':
    main()

