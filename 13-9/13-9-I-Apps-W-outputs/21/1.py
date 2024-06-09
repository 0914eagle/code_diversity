
def get_min_radius(points):
    x_coords, y_coords = zip(*points)
    x_avg, y_avg = sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords)
    distances = [(x - x_avg) ** 2 + (y - y_avg) ** 2 for x, y in points]
    return (sum(distances) / len(distances)) ** 0.5

