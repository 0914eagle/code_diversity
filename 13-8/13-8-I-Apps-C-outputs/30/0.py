
def canyon_mapping(n, k, polygon):
    # Sort the polygon vertices in clockwise order
    polygon.sort(key=lambda x: x[0] * x[1])
    # Calculate the area of the polygon
    area = abs(sum(x1 * y2 - x2 * y1 for x1, y1, x2, y2 in zip(polygon, polygon[1:] + polygon[:1])))
    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5
    # Return the rounded side length to two decimal places
    return round(side_length, 2)

