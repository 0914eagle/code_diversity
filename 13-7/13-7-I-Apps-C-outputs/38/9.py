
import math

def get_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        x, h = building
        total_hours += (h / 180) * (180 / math.pi) * (math.acos(x / 180) - math.acos((x - 180) / 180))
    return total_hours

def get_sunlight_hours_per_building(buildings):
    total_hours = get_sunlight_hours(buildings)
    return [total_hours / len(buildings) for _ in range(len(buildings))]

def main():
    num_buildings = int(input())
    buildings = []
    for _ in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    print(*get_sunlight_hours_per_building(buildings), sep='\n')

if __name__ == '__main__':
    main()

