
def get_closest_distance(vehicle_locations):
    # Sort the vehicles by their location
    sorted_vehicles = sorted(vehicle_locations, key=lambda x: x[0])

    # Initialize the closest distance to a large value
    closest_distance = 100000

    # Iterate through the vehicles and calculate the distance between them
    for i in range(len(sorted_vehicles) - 1):
        distance = abs(sorted_vehicles[i + 1][0] - sorted_vehicles[i][0])
        closest_distance = min(closest_distance, distance)

    return closest_distance

def main():
    num_vehicles = int(input())
    vehicle_locations = []
    for i in range(num_vehicles):
        x, v = map(int, input().split())
        vehicle_locations.append((x, v))
    print(get_closest_distance(vehicle_locations))

if __name__ == '__main__':
    main()

