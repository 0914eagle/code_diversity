
def solve(W, H, x, y):
    area_1 = x * y
    area_2 = (W-x) * (H-y)
    area_3 = W * H - area_1 - area_2
    if area_1 >= area_2 and area_1 >= area_3:
        return area_1, 0
    elif area_2 >= area_1 and area_2 >= area_3:
        return area_2, 0
    else:
        return area_3, 1

