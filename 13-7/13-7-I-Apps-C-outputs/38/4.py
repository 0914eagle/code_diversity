
def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        total_hours += building[1] / 180
    return total_hours

def get_sunlight_hours_per_building(buildings):
    # Calculate the number of hours of sunlight for each building
    hours_per_building = []
    for building in buildings:
        hours_per_building.append(building[1] / 180)
    return hours_per_building

def main():
    # Get the number of buildings
    n = int(input())
    # Get the locations and heights of the buildings
    buildings = []
    for i in range(n):
        x, h = map(int, input().split())
        buildings.append([x, h])
    # Calculate the total number of hours of sunlight
    total_hours = get_sunlight_hours(buildings)
    # Calculate the number of hours of sunlight for each building
    hours_per_building = get_sunlight_hours_per_building(buildings)
    # Print the number of hours of sunlight for each building
    for hour in hours_per_building:
        print(hour)

if __name__ == '__main__':
    main()

