
def get_sunlight_hours(buildings):
    # Calculate the total number of hours of sunlight
    total_hours = 0
    for building in buildings:
        total_hours += building[1] * building[0] / 180
    return total_hours

def get_peak_sunlight_hours(buildings):
    # Calculate the number of hours for which the peak of each building is bathed in sunlight
    peak_hours = []
    for building in buildings:
        hours = building[1] * building[0] / 180
        peak_hours.append(hours)
    return peak_hours

def main():
    # Read the input
    num_buildings = int(input())
    buildings = []
    for i in range(num_buildings):
        x, h = map(int, input().split())
        buildings.append((x, h))
    
    # Calculate the total number of hours of sunlight and the number of hours for which the peak of each building is bathed in sunlight
    total_hours = get_sunlight_hours(buildings)
    peak_hours = get_peak_sunlight_hours(buildings)
    
    # Print the output
    for hours in peak_hours:
        print(f"{hours:.4f}")
    
    return total_hours

if __name__ == '__main__':
    main()

