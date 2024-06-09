
def solve(polygon, area):
    # Calculate the current area of the polygon
    current_area = calculate_area(polygon)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = area / current_area

    # Resize the polygon and return the new polygon coordinates
    return resize_polygon(polygon, scaling_factor)

def calculate_area(polygon):
    # Calculate the area of the polygon using the shoelace formula
    area = 0.5 * abs(sum(x1 * y2 - x2 * y1 for x1, y1, x2, y2 in zip(polygon, polygon[1:] + polygon[:1])))
    return area

def resize_polygon(polygon, scaling_factor):
    # Resize the polygon by scaling up or down all the coordinates
    return [(x * scaling_factor, y * scaling_factor) for x, y in polygon]

