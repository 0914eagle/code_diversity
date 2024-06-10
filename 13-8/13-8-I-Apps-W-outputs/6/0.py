
def get_min_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance to a large value
    min_distance = 100000
    
    # Iterate over the vehicles
    for i in range(len(vehicles) - 1):
        # Calculate the distance between the current vehicle and the next vehicle
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        
        # Update the minimum distance if necessary
        min_distance = min(min_distance, distance)
    
    return min_distance

def main():
    # Read the number of vehicles
    n = int(input())
    
    # Read the position and velocity of each vehicle
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    
    # Calculate the minimum distance
    min_distance = get_min_distance(vehicles)
    
    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

