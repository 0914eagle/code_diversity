
import math

def get_min_radius(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_max = max(x_coords)
    x_min = min(x_coords)
    y_max = max(y_coords)
    y_min = min(y_coords)
    x_mid = (x_max - x_min) / 2.0 + x_min
    y_mid = (y_max - y_min) / 2.0 + y_min
    radius = math.sqrt((x_mid - x_min) ** 2 + (y_mid - y_min) ** 2)
    return radius

points = []
for _ in range(int(input())):
    points.append(tuple(map(int, input().split())))

print(get_min_radius(points))

