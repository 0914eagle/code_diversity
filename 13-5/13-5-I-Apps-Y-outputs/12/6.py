
def larger_rectangle(A, B, C, D):
    area_1 = A * B
    area_2 = C * D
    if area_1 > area_2:
        return area_1
    elif area_1 < area_2:
        return area_2
    else:
        return area_1

