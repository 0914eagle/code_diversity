
import math

def get_sunlight_hours(buildings):
    total_hours = 0
    for building in buildings:
        top_angle = building[1] / 2
        bottom_angle = math.radians(180) - top_angle
        hour_angle = 2 * math.sin(bottom_angle)
        total_hours += hour_angle
    return total_hours

def get_building_hours(buildings):
    building_hours = []
    for building in buildings:
        top_angle = building[1] / 2
        bottom_angle = math.radians(180) - top_angle
        hour_angle = 2 * math.sin(bottom_angle)
        building_hours.append(hour_angle)
    return building_hours

def main():
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        building = [int(x) for x in input().split()]
        buildings.append(building)
    total_hours = get_sunlight_hours(buildings)
    building_hours = get_building_hours(buildings)
    for hour in building_hours:
        print(f"{hour:.4f}")

if __name__ == '__main__':
    main()

