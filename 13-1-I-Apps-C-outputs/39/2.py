
import math

def get_watered_area(a, b, c, d):
    # Calculate the total area of the courtyard
    total_area = 4 * math.pow(10, 4)

    # Calculate the area of the triangle formed by the bottom right sprinkler and the bottom wall
    bottom_right_angle = math.radians(a)
    bottom_right_area = (math.tan(bottom_right_angle) * math.pow(10, 4)) / 2

    # Calculate the area of the triangle formed by the top right sprinkler and the top wall
    top_right_angle = math.radians(b)
    top_right_area = (math.tan(top_right_angle) * math.pow(10, 4)) / 2

    # Calculate the area of the triangle formed by the top left sprinkler and the left wall
    top_left_angle = math.radians(c)
    top_left_area = (math.tan(top_left_angle) * math.pow(10, 4)) / 2

    # Calculate the area of the triangle formed by the bottom left sprinkler and the bottom wall
    bottom_left_angle = math.radians(d)
    bottom_left_area = (math.tan(bottom_left_angle) * math.pow(10, 4)) / 2

    # Calculate the total area watered by the sprinklers
    total_watered_area = bottom_right_area + top_right_area + top_left_area + bottom_left_area

    # Calculate the proportion of the courtyard that is watered
    watered_proportion = total_watered_area / total_area

    return watered_proportion

