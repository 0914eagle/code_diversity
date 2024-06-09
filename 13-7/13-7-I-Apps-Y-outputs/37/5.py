
def solve(polygon, area):
    # Calculate the current area of the polygon
    current_area = calculate_area(polygon)

    # Calculate the scaling factor needed to achieve the desired area
    scaling_factor = area / current_area

    # Scale the polygon
    scaled_polygon = []
    for point in polygon:
        scaled_polygon.append((point[0] * scaling_factor, point[1] * scaling_factor))

    # Return the scaled polygon
    return scaled_polygon

def calculate_area(polygon):
    # Calculate the area of the polygon
    area = 0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2

    # Return the area
    return area

