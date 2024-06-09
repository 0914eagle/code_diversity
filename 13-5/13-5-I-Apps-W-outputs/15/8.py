
def is_respectable_set(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    x_coords.sort()
    y_coords.sort()

    if len(set(x_coords)) != 3 or len(set(y_coords)) != 3:
        return "ugly"

    x1, x2, x3 = x_coords
    y1, y2, y3 = y_coords

    if x1 + x2 + x3 != 3 or y1 + y2 + y3 != 3:
        return "ugly"

    return "respectable"

