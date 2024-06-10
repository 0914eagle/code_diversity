
def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance as the difference between the first and last vehicle's position
    min_distance = abs(vehicles[-1][0] - vehicles[0][0])
    
    # Loop through the vehicles and calculate the distance between each pair of vehicles
    for i in range(len(vehicles) - 1):
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        min_distance = min(min_distance, distance)
    
    return min_distance

def main():
    num_vehicles = int(input())
    vehicles = []
    for i in range(num_vehicles):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    print(get_closest_distance(vehicles))

if __name__ == '__main__':
    main()

