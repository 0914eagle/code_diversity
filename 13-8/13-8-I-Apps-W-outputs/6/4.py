
def get_min_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance
    min_distance = 0
    
    # Iterate over the vehicles
    for i in range(len(vehicles) - 1):
        # Calculate the distance between the current vehicle and the next vehicle
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        
        # Update the minimum distance
        min_distance = max(min_distance, distance)
    
    return min_distance

def main():
    # Read the number of vehicles
    n = int(input())
    
    # Read the positions and velocities of the vehicles
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    
    # Find the minimum distance that covers all of the vehicles
    min_distance = get_min_distance(vehicles)
    
    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

