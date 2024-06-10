
import math

def circle_area_euclidian(radius):
    return math.pi * radius ** 2

def circle_area_taxicab(radius):
    return 4 * radius ** 2

if __name__ == '__main__':
    radius = int(input())
    print(circle_area_euclidian(radius))
    print(circle_area_taxicab(radius))

