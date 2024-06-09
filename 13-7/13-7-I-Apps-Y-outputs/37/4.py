
def solve(points, area):
    # Calculate the current area of the polygon
    current_area = 0
    for i in range(len(points)):
        current_area += points[i][0] * points[(i+1)%len(points)][1]
        current_area -= points[i][1] * points[(i+1)%len(points)][0]
    current_area = abs(current_area) / 2

    # Calculate the ratio of the current area to the desired area
    ratio = area / current_area

    # Scale the polygon by the ratio
    scaled_points = []
    for point in points:
        scaled_points.append((point[0] * ratio, point[1] * ratio))

    # Return the scaled points
    return scaled_points

