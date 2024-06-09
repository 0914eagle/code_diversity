
def solve(points, area):
    # Calculate the current area of the polygon
    current_area = abs(0.5 * sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in zip(points + points[:1], points[:-1] + points[-1:])))

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = area / current_area

    # Resize the polygon by applying the scaling factor to all points
    resized_points = [(x * scaling_factor, y * scaling_factor) for (x, y) in points]

    # Return the resized polygon
    return resized_points

