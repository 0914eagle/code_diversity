
def get_max_area(W, H, x, y):
    area_1 = x * y
    area_2 = (W-x) * (H-y)
    area_3 = W * H - area_1 - area_2
    max_area = max(area_1, area_2, area_3)
    if area_1 == max_area:
        return area_1, 1
    elif area_2 == max_area:
        return area_2, 1
    else:
        return area_3, 0

