
def is_respectable(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    x_coords.sort()
    y_coords.sort()

    if len(set(x_coords)) != 3 or len(set(y_coords)) != 3:
        return "ugly"

    for i in range(3):
        for j in range(3):
            if (x_coords[i], y_coords[j]) not in points:
                return "ugly"

    return "respectable"

