
import math

def get_min_damage(x_s, y_s, s_s, r_i, r_f, x_a, y_a, s_a):
    # Calculate the distance between Anthony and the center of the safety zone
    dist = math.sqrt((x_a - x_s) ** 2 + (y_a - y_s) ** 2)

    # Calculate the time it takes for Anthony to reach the safety zone
    t = dist / s_a

    # Calculate the radius of the safety zone at the time Anthony reaches it
    r = r_i - s_s * t

    # Calculate the minimum amount of damage Anthony will take
    d = r_f - r

    return d

