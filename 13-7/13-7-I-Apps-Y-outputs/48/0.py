
import math

def get_area_euclidian_circle(radius):
    return math.pi * radius ** 2

def get_area_taxicab_circle(radius):
    return 4 * radius ** 2

if __name__ == '__main__':
    radius = float(input())
    print(get_area_euclidian_circle(radius))
    print(get_area_taxicab_circle(radius))

