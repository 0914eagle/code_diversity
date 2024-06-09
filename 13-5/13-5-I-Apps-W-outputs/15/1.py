
def is_respectable(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    x_coords.sort()
    y_coords.sort()

    if len(set(x_coords)) != 3 or len(set(y_coords)) != 3:
        return "ugly"

    if (x_coords[0], y_coords[0]) in points and (x_coords[2], y_coords[2]) in points:
        return "ugly"

    return "respectable"

