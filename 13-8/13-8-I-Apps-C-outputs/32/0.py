
import math

def get_max_pickles(sandwich_radius, pickle_radius, num_pickles, max_area_coverage):
    area_coverage_percent = max_area_coverage / 100
    max_pickles = 0
    for i in range(1, num_pickles + 1):
        area_covered = get_area_covered(sandwich_radius, pickle_radius, i)
        if area_covered / get_sandwich_area(sandwich_radius) <= area_coverage_percent:
            max_pickles = i
    return max_pickles

def get_area_covered(sandwich_radius, pickle_radius, num_pickles):
    angle_between_pickles = 360 / num_pickles
    total_angle = angle_between_pickles * num_pickles
    arc_length = 2 * math.pi * pickle_radius * total_angle / 360
    return arc_length ** 2

def get_sandwich_area(sandwich_radius):
    return math.pi * sandwich_radius ** 2

if __name__ == '__main__':
    sandwich_radius, pickle_radius, num_pickles, max_area_coverage = map(float, input().split())
    print(get_max_pickles(sandwich_radius, pickle_radius, num_pickles, max_area_coverage))

