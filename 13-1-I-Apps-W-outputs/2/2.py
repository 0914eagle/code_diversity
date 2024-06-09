
import math

def solve(l_3, l_4, l_5):
    # Calculate the volume of the triangular pyramid
    v_3 = (l_3 * l_3 * l_3) / (3 * math.sqrt(2))

    # Calculate the volume of the quadrangular pyramid
    v_4 = (l_4 * l_4 * l_4) / 3

    # Calculate the volume of the pentagonal pyramid
    v_5 = (l_5 * l_5 * l_5) / (3 * math.sqrt(5))

    # Calculate the total volume
    total_volume = v_3 + v_4 + v_5

    return total_volume

