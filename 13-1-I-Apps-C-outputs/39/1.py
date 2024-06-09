
import math

def get_watered_area(a, b, c, d):
    # Calculate the total area of the courtyard
    total_area = 4 * (a + b + c + d) / 2

    # Calculate the area of the triangles formed by the sprinklers
    area_1 = (a * b) / 2
    area_2 = (b * c) / 2
    area_3 = (c * d) / 2
    area_4 = (d * a) / 2

    # Calculate the total area watered by the sprinklers
    watered_area = area_1 + area_2 + area_3 + area_4

    # Return the proportion of the watered area
    return watered_area / total_area

