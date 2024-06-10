
import math

def get_hours_of_sunlight(buildings):
    total_hours = 0
    for building in buildings:
        total_hours += building[1] * math.cos(math.radians(building[0]))
    return total_hours

def main():
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append([x, h])
    print(get_hours_of_sunlight(buildings))

if __name__ == '__main__':
    main()

