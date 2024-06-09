
def get_max_area(W, H, x, y):
    area_1 = x * y
    area_2 = (W-x) * (H-y)
    area_3 = W * H - area_1 - area_2
    max_area = max(area_1, area_2, area_3)
    return max_area

