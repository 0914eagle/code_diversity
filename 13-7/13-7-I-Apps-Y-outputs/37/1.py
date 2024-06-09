
def solve(polygon, area):
    # Calculate the current area of the polygon
    current_area = get_area(polygon)

    # Calculate the scaling factor to achieve the desired area
    scaling_factor = area / current_area

    # Scale the polygon
    scaled_polygon = [(x * scaling_factor, y * scaling_factor) for x, y in polygon]

    # Return the scaled polygon
    return scaled_polygon

def get_area(polygon):
    # Calculate the area of the polygon using the shoelace formula
    area = 0.5 * abs(sum(x1 * y2 - x2 * y1 for x1, y1, x2, y2 in zip(polygon, polygon[1:] + polygon[:1])))

    # Return the area
    return area

