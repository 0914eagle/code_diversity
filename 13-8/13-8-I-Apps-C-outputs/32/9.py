
import math

def get_area_of_sandwich(radius):
    return math.pi * radius ** 2

def get_area_of_pickle(radius):
    return math.pi * radius ** 2

def get_max_pickles(sandwich_radius, pickle_radius, n, z):
    area_of_sandwich = get_area_of_sandwich(sandwich_radius)
    area_of_pickle = get_area_of_pickle(pickle_radius)
    max_pickles = 0
    for i in range(1, n + 1):
        area_covered = i * area_of_pickle
        if area_covered / area_of_sandwich <= z / 100:
            max_pickles = i
        else:
            break
    return max_pickles

def main():
    sandwich_radius, pickle_radius, n, z = map(float, input().split())
    print(get_max_pickles(sandwich_radius, pickle_radius, n, z))

if __name__ == '__main__':
    main()

