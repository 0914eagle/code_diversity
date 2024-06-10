
import math

def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance and the current position
    min_distance = 0
    current_position = 0
    
    # Loop through the vehicles and calculate the closest distance
    for vehicle in vehicles:
        # Calculate the distance between the current vehicle and the previous vehicle
        distance = vehicle[0] - current_position
        
        # If the distance is greater than the minimum distance, update the minimum distance
        if distance > min_distance:
            min_distance = distance
        
        # Update the current position
        current_position = vehicle[0]
    
    return min_distance

def main():
    # Read the number of vehicles
    n = int(input())
    
    # Read the positions and velocities of the vehicles
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    
    # Calculate the closest distance
    min_distance = get_closest_distance(vehicles)
    
    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

