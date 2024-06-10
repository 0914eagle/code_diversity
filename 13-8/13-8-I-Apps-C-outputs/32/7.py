
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_total_area(sandwich_radius, pickle_radius):
    return calculate_area(sandwich_radius) - calculate_area(pickle_radius)

def place_pickles(sandwich_radius, pickle_radius, n, z):
    total_area = calculate_total_area(sandwich_radius, pickle_radius)
    area_covered = 0
    pickles_placed = 0
    while area_covered <= z * total_area / 100 and pickles_placed < n:
        area_covered += calculate_area(pickle_radius)
        pickles_placed += 1
    return pickles_placed

def main():
    sandwich_radius, pickle_radius, n, z = map(float, input().split())
    print(place_pickles(sandwich_radius, pickle_radius, n, z))

if __name__ == '__main__':
    main()

