
def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the closest distance to infinity
    closest_distance = float('inf')
    
    # Iterate over the vehicles
    for i in range(len(vehicles) - 1):
        # Get the position and velocity of the current vehicle
        x1, v1 = vehicles[i]
        
        # Get the position and velocity of the next vehicle
        x2, v2 = vehicles[i + 1]
        
        # Calculate the distance between the current and next vehicle
        distance = abs(x2 - x1)
        
        # Calculate the time it takes for the vehicles to collide
        time = distance / ((v1 + v2) / 2)
        
        # Update the closest distance if necessary
        closest_distance = min(closest_distance, distance / time)
    
    return closest_distance

def main():
    # Read the number of vehicles
    n = int(input())
    
    # Read the position and velocity of each vehicle
    vehicles = []
    for _ in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    
    # Find the closest distance
    closest_distance = get_closest_distance(vehicles)
    
    # Print the result
    print(closest_distance)

if __name__ == '__main__':
    main()

