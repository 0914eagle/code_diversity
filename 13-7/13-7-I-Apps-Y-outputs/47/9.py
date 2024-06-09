
def get_maximum_area(w, h, x, y):
    area_1 = x * y
    area_2 = (w - x) * y
    area_3 = x * (h - y)
    area_4 = (w - x) * (h - y)
    max_area = max(area_1, area_2, area_3, area_4)
    return max_area

