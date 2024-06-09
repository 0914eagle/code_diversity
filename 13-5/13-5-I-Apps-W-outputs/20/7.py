
def get_max_value(A, B, N):
    max_value = 0
    for x in range(N+1):
        floor_Ax_B = int(A*x/B)
        A_floor_x_B = A*int(x/B)
        value = floor_Ax_B - A_floor_x_B
        if value > max_value:
            max_value = value
    return max_value

