
import math

def get_euclidian_area(r):
    return math.pi * r ** 2

def get_taxicab_area(r):
    return 2 * math.pi * r

if __name__ == '__main__':
    r = int(input())
    print(get_euclidian_area(r))
    print(get_taxicab_area(r))

