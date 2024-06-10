
import math

def get_circle_area(radius):
    return math.pi * radius ** 2

def get_circle_perimeter(radius):
    return 2 * math.pi * radius

def get_max_pickles(sandwich_radius, pickle_radius, num_pickles, max_area):
    max_area_covered = 0
    max_pickles = 0
    for i in range(1, num_pickles + 1):
        area_covered = 0
        perimeter = get_circle_perimeter(pickle_radius)
        for j in range(i):
            area_covered += get_circle_area(pickle_radius)
            perimeter += 2 * math.pi * pickle_radius
        if area_covered / get_circle_area(sandwich_radius) * 100 <= max_area:
            if area_covered > max_area_covered:
                max_area_covered = area_covered
                max_pickles = i
    return max_pickles

def main():
    sandwich_radius, pickle_radius, num_pickles, max_area = map(float, input().split())
    print(get_max_pickles(sandwich_radius, pickle_radius, num_pickles, max_area))

if __name__ == '__main__':
    main()

