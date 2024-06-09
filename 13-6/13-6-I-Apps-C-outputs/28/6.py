
def get_area_of_carpet(a, b, c):
    if a + b + c > 100:
        return -1
    area = (a * b * c) / 2
    return round(area, 3)

