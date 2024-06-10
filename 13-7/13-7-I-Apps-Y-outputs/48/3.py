
import math

def circle_area_euclidian(r):
    return math.pi * r ** 2

def circle_area_taxicab(r):
    return 2 * math.pi * r

if __name__ == '__main__':
    r = int(input())
    print(circle_area_euclidian(r))
    print(circle_area_taxicab(r))

