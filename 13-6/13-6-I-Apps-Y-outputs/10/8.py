
def restore_square(x1, y1, x2, y2):
    x3 = y2 - y1
    y3 = x1 - x2
    x4 = x3 + x1
    y4 = y3 + y1
    return x3, y3, x4, y4

