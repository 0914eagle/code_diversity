
import math

def get_euclidian_circle_area(radius):
    return math.pi * radius ** 2

def get_taxicab_circle_area(radius):
    return 2 * radius ** 2

if __name__ == '__main__':
    radius = float(input())
    print(get_euclidian_circle_area(radius))
    print(get_taxicab_circle_area(radius))

