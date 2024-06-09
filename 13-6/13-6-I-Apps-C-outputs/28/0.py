
import math

def get_area(a, b, c):
    if a + b + c > 100:
        return -1
    
    area = (a * b * c) / (4 * math.tan(math.pi / 3))
    return round(area, 3)

