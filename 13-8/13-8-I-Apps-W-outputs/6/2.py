
def get_min_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance to a large value
    min_distance = 100000
    
    # Iterate over the vehicles
    for i in range(len(vehicles)-1):
        # Get the current and next vehicle
        current_vehicle = vehicles[i]
        next_vehicle = vehicles[i+1]
        
        # Calculate the distance between the current and next vehicle
        distance = abs(next_vehicle[0] - current_vehicle[0])
        
        # Update the minimum distance if necessary
        if distance < min_distance:
            min_distance = distance
    
    return min_distance

def main():
    # Read the number of vehicles
    n = int(input())
    
    # Read the positions and velocities of the vehicles
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    
    # Call the get_min_distance function
    min_distance = get_min_distance(vehicles)
    
    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

