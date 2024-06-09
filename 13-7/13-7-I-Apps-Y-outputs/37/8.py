
def solve(cookie_cutter, area):
    # Calculate the current area of the cookie cutter
    current_area = calculate_area(cookie_cutter)

    # Calculate the ratio of the current area to the desired area
    ratio = area / current_area

    # Create a new list to store the resized cookie cutter
    resized_cookie_cutter = []

    # Loop through the original cookie cutter and resize each point
    for point in cookie_cutter:
        resized_point = (point[0] * ratio, point[1] * ratio)
        resized_cookie_cutter.append(resized_point)

    # Return the resized cookie cutter
    return resized_cookie_cutter

def calculate_area(cookie_cutter):
    # Initialize the area to 0
    area = 0

    # Loop through the cookie cutter and calculate the area
    for i in range(len(cookie_cutter)):
        # Calculate the area of the triangle created by the current point and the next two points
        triangle_area = calculate_triangle_area(cookie_cutter[i], cookie_cutter[(i + 1) % len(cookie_cutter)], cookie_cutter[(i + 2) % len(cookie_cutter)])

        # Add the area of the triangle to the total area
        area += triangle_area

    # Return the total area
    return area

def calculate_triangle_area(p1, p2, p3):
    # Calculate the area of the triangle
    area = 0.5 * abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p1[1] * p2[0] - p2[1] * p3[0] - p3[1] * p1[0])

    # Return the area
    return area

