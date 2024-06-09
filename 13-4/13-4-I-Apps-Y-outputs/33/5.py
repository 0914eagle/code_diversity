
def f1(polygon, area):
    # Calculate the current area of the polygon
    current_area = f2(polygon)

    # Calculate the scaling factor to resize the polygon to the desired area
    scaling_factor = (area / current_area) ** 0.5

    # Resize the polygon
    resized_polygon = [(x * scaling_factor, y * scaling_factor) for x, y in polygon]

    return resized_polygon

def f2(polygon):
    # Calculate the area of the polygon
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2

if __name__ == '__main__':
    polygon = [(0, 0), (1, 1), (0, 2)]
    area = 4
    resized_polygon = f1(polygon, area)
    print(resized_polygon)

