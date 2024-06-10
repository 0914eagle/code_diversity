
import math

def calculate_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        total_hours += calculate_building_sunlight_hours(building)
    return total_hours

def calculate_building_sunlight_hours(building):
    x, h = building
    return (180 / (math.pi * h ** 2)) * (180 - 2 * x)

def main():
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    print(calculate_sunlight_hours(buildings))

if __name__ == '__main__':
    main()

