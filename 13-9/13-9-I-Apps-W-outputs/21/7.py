
import math

def solve(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    radius = 0.5 * math.sqrt((x_max-x_min)**2 + (y_max-y_min)**2)
    return radius

