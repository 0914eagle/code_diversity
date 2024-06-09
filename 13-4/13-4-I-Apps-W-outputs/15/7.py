
def is_possible(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            count = 0
            for point in points:
                if point[0] == x or point[1] == y:
                    count += 1
            if count == len(points):
                return "YES"
    return "NO"

