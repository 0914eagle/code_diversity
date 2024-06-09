
import math

def max_pickles(s, r, n, z):
    area_sandwich = math.pi * s ** 2
    area_pickle = math.pi * r ** 2
    max_area_pickles = area_sandwich * z / 100
    max_pickles = int(max_area_pickles / area_pickle)
    return min(max_pickles, n)

