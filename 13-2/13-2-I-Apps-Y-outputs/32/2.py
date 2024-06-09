
import math

def get_percentage_cheese(radius, crust_thickness):
    total_area = math.pi * radius ** 2
    crust_area = math.pi * (radius - crust_thickness) ** 2
    cheese_area = total_area - crust_area
    return 100 * cheese_area / total_area

if __name__ == '__main__':
    radius, crust_thickness = map(int, input().split())
    print(get_percentage_cheese(radius, crust_thickness))

