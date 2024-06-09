
def get_maximum_value(a, b, n):
    max_value = 0
    for x in range(n+1):
        floor_ax_b = a*x//b
        floor_x_b = x//b
        value = floor_ax_b - a*floor_x_b
        if value > max_value:
            max_value = value
    return max_value

