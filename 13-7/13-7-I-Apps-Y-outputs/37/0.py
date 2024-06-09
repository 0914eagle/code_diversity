
def solve(points, area):
    # Calculate the current area of the polygon
    current_area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        current_area += x1 * y2 - x2 * y1
    current_area = abs(current_area) / 2

    # Calculate the required scaling factor to achieve the desired area
    scaling_factor = area / current_area

    # Scale the polygon points
    scaled_points = []
    for x, y in points:
        scaled_points.append((x * scaling_factor, y * scaling_factor))

    # Ensure that the scaled polygon touches the x- and y-axes
    min_x = min(scaled_points, key=lambda x: x[0])[0]
    min_y = min(scaled_points, key=lambda y: y[1])[1]
    for i in range(len(scaled_points)):
        scaled_points[i] = (scaled_points[i][0] - min_x, scaled_points[i][1] - min_y)

    return scaled_points

