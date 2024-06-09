
def get_max_area(w, h, x, y):
    area_1 = x * y
    area_2 = (w-x) * (h-y)
    area_3 = w * h - area_1 - area_2
    max_area = max(area_1, area_2, area_3)
    return max_area

