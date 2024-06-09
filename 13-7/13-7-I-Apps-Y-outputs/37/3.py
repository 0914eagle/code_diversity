
def solve(points, area):
    # Calculate the area of the original polygon
    original_area = calculate_area(points)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (area / original_area) ** 0.5

    # Resize the polygon
    resized_points = []
    for point in points:
        resized_points.append((point[0] * scaling_factor, point[1] * scaling_factor))

    # Return the resized polygon
    return resized_points

def calculate_area(points):
    # Calculate the area of the polygon using the shoelace formula
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2

    # Return the area
    return area

