
def find_min_radius(points):
    x_coords, y_coords = zip(*points)
    x_avg, y_avg = sum(x_coords) / len(points), sum(y_coords) / len(points)
    distances = [(x - x_avg) ** 2 + (y - y_avg) ** 2 for x, y in points]
    return math.sqrt(min(distances))

