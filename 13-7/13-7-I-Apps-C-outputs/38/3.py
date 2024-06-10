
import math

def get_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        x, h = building
        angle = (h / 180) * math.pi
        total_hours += 2 * angle
    return total_hours

def solve(buildings):
    total_hours = get_sunlight_hours(buildings)
    return total_hours

if __name__ == '__main__':
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    print(solve(buildings))

