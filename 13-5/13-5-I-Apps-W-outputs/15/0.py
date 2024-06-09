
def is_respectable_set(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    # Check if all x-coordinates are distinct
    if len(set(x_coords)) != len(x_coords):
        return "ugly"

    # Check if all y-coordinates are distinct
    if len(set(y_coords)) != len(y_coords):
        return "ugly"

    # Check if there are three distinct horizontal and three distinct vertical lines
    horizontal_lines = set()
    vertical_lines = set()
    for point in points:
        horizontal_lines.add(point[1])
        vertical_lines.add(point[0])
    if len(horizontal_lines) != 3 or len(vertical_lines) != 3:
        return "ugly"

    # Check if the set consists of all points except for the average of the nine points
    average_x = sum(x_coords) / len(x_coords)
    average_y = sum(y_coords) / len(y_coords)
    if (average_x, average_y) in points:
        return "ugly"

    return "respectable"

