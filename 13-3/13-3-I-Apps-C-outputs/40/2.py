
import math

def get_max_pickles(s, r, n, z):
    area_sandwich = math.pi * s ** 2
    area_pickle = math.pi * r ** 2
    max_area_pickles = area_sandwich * z / 100
    max_pickles = 0
    for i in range(n + 1):
        area_covered = i * area_pickle
        if area_covered <= max_area_pickles:
            max_pickles = i
        else:
            break
    return max_pickles

