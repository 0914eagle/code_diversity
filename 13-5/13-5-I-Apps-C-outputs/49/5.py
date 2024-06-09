
import math

def get_center(points):
    point_1, point_2, point_3, point_4 = points
    x1, y1, z1 = point_1
    x2, y2, z2 = point_2
    x3, y3, z3 = point_3
    x4, y4, z4 = point_4

    # Create two vectors from the points
    v1 = [x2 - x1, y2 - y1, z2 - z1]
    v2 = [x3 - x1, y3 - y1, z3 - z1]
    v3 = [x4 - x1, y4 - y1, z4 - z1]

    # Calculate the cross product of the vectors
    cross_product = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]

    # Calculate the dot product of the vectors
    dot_product = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

    # Calculate the angle between the vectors
    angle = math.acos(dot_product / (math.sqrt(dot_product ** 2) * math.sqrt(cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2)))

    # Calculate the length of the vectors
    length_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
    length_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2)
    length_v3 = math.sqrt(v3[0] ** 2 + v3[1] ** 2 + v3[2] ** 2)

    # Calculate the radius of the sphere
    radius = (length_v1 * length_v2 * length_v3) / (2 * math.sin(angle))

    # Calculate the center of the sphere
    center = [(point_1[0] + point_2[0] + point_3[0] + point_4[0]) / 4, (point_1[1] + point_2[1] + point_3[1] + point_4[1]) / 4, (point_1[2] + point_2[2] + point_3[2] + point_4[2]) / 4]

    return center, radius

