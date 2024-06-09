
import math

def get_watered_area(a, b, c, d):
    # Calculate the total area of the courtyard
    total_area = 4 * (a + b + c + d) / 2

    # Calculate the area of the triangle formed by the bottom right sprinkler and the bottom wall
    bottom_right_triangle_area = (a * b) / 2

    # Calculate the area of the triangle formed by the top right sprinkler and the top wall
    top_right_triangle_area = (b * c) / 2

    # Calculate the area of the triangle formed by the top left sprinkler and the left wall
    top_left_triangle_area = (c * d) / 2

    # Calculate the area of the triangle formed by the bottom left sprinkler and the bottom wall
    bottom_left_triangle_area = (d * a) / 2

    # Calculate the total area of the triangles
    total_triangle_area = bottom_right_triangle_area + top_right_triangle_area + top_left_triangle_area + bottom_left_triangle_area

    # Calculate the proportion of the total area that is watered
    watered_area = total_triangle_area / total_area

    return watered_area

