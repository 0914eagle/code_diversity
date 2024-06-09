
def solve(points, area):
    # Calculate the original area of the polygon
    original_area = get_area(points)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (area / original_area)**0.5

    # Resize the polygon
    resized_points = [(x * scaling_factor, y * scaling_factor) for x, y in points]

    # Move the resized polygon to the north-east quadrant
    min_x = min(x for x, _ in resized_points)
    min_y = min(y for _, y in resized_points)
    resized_points = [(x - min_x, y - min_y) for x, y in resized_points]

    return resized_points

def get_area(points):
    # Calculate the area of a polygon using the shoelace formula
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

