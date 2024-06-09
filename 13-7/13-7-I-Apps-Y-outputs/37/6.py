
def solve(points, area):
    # Calculate the current area of the polygon
    current_area = calculate_area(points)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (area / current_area) ** 0.5

    # Resize the polygon
    resized_points = []
    for point in points:
        resized_points.append((point[0] * scaling_factor, point[1] * scaling_factor))

    return resized_points

def calculate_area(points):
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2
    return area

