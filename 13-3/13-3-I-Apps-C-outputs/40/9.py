
import math

def max_pickles(s, r, n, z):
    area_sandwich = math.pi * s ** 2
    area_pickle = math.pi * r ** 2
    max_area_covered = area_sandwich * z / 100
    max_pickles = 0
    for i in range(n + 1):
        area_covered = 0
        for j in range(i):
            area_covered += area_pickle
            if area_covered > max_area_covered:
                break
        if area_covered <= max_area_covered:
            max_pickles = i
    return max_pickles

