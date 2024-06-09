
def larger_rectangle(A, B, C, D):
    rectangle_1 = A * B
    rectangle_2 = C * D
    if rectangle_1 > rectangle_2:
        return rectangle_1
    elif rectangle_2 > rectangle_1:
        return rectangle_2
    else:
        return rectangle_1

