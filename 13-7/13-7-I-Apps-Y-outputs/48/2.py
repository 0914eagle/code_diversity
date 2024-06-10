
import math

def get_area_circle_euclidian(radius):
    return math.pi * radius ** 2

def get_area_circle_taxicab(radius):
    return 2 * radius ** 2

if __name__ == '__main__':
    radius = int(input())
    print(get_area_circle_euclidian(radius))
    print(get_area_circle_taxicab(radius))

