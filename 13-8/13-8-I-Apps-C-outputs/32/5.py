
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_pickles(sandwich_area, pickle_area, max_coverage):
    total_pickles = 0
    current_area = 0
    while current_area < sandwich_area * max_coverage / 100:
        total_pickles += 1
        current_area += pickle_area
    return total_pickles

def main():
    sandwich_radius, pickle_radius = map(float, input().split())
    num_pickles, max_coverage = map(int, input().split())
    sandwich_area = calculate_area(sandwich_radius)
    pickle_area = calculate_area(pickle_radius)
    print(calculate_pickles(sandwich_area, pickle_area, max_coverage))

if __name__ == '__main__':
    main()

