
def solve(A, B, C, D):
    rect1_area = A * B
    rect2_area = C * D
    if rect1_area > rect2_area:
        return rect1_area
    elif rect1_area < rect2_area:
        return rect2_area
    else:
        return rect1_area

