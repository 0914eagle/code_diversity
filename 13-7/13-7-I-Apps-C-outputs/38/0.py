
import math

def calculate_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        x, h = building
        angle = (h / 2) * math.pi / 180
        total_hours += angle
    return total_hours

def main():
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    total_hours = calculate_sunlight_hours(buildings)
    print(f"{total_hours:.4f}")

if __name__ == '__main__':
    main()

