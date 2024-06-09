
def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance as the maximum possible distance
    min_distance = 100000
    
    # Iterate over the vehicles
    for i in range(len(vehicles) - 1):
        # Calculate the distance between the current vehicle and the next vehicle
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        
        # Update the minimum distance if necessary
        min_distance = min(min_distance, distance)
    
    return min_distance

