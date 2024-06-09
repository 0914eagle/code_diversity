
import math

def get_max_pickles(s, r, n, z):
    area_sandwich = math.pi * s ** 2
    area_pickle = math.pi * r ** 2
    max_pickles = 0
    for i in range(1, n + 1):
        area_covered = i * area_pickle
        if area_covered / area_sandwich * 100 <= z:
            max_pickles = i
    return max_pickles

