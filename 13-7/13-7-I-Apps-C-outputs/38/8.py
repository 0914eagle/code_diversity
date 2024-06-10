
import math

def get_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        x, h = building
        total_hours += (180 / (2 * math.pi)) * (h / x)
    return total_hours

def main():
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    print(get_sunlight_hours(buildings))

if __name__ == '__main__':
    main()

