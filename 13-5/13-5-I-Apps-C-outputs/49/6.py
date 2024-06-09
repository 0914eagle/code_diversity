
import math

def get_center(points):
    point1, point2, point3, point4 = points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    x4, y4, z4 = point4

    # Create two vectors from the points
    v1 = [x2 - x1, y2 - y1, z2 - z1]
    v2 = [x3 - x1, y3 - y1, z3 - z1]
    v3 = [x4 - x1, y4 - y1, z4 - z1]

    # Calculate the cross product of the vectors
    cross_product = [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

    # Calculate the dot product of the vectors
    dot_product = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    # Calculate the angle between the vectors
    angle = math.acos(dot_product / (math.sqrt(dot_product ** 2) * math.sqrt(cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2)))

    # Calculate the distance between the center and point1
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    # Calculate the coordinates of the center
    x_center = x1 + (distance * math.cos(angle)) / math.sin(angle)
    y_center = y1 + (distance * math.cos(angle)) / math.sin(angle)
    z_center = z1 + (distance * math.cos(angle)) / math.sin(angle)

    return [x_center, y_center, z_center]

