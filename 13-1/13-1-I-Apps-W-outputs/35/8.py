
def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance as the maximum possible distance
    min_distance = 100000
    
    # Iterate over the vehicles
    for i in range(len(vehicles) - 1):
        # Get the position and velocity of the current vehicle
        pos_i, vel_i = vehicles[i]
        
        # Get the position and velocity of the next vehicle
        pos_j, vel_j = vehicles[i + 1]
        
        # Calculate the distance between the two vehicles
        distance = abs(pos_i - pos_j)
        
        # Calculate the time it takes for the vehicles to pass each other
        time = distance / ((vel_i + vel_j) / 2)
        
        # Calculate the minimum distance required to cover all vehicles at that time
        min_distance = min(min_distance, distance / time)
    
    return min_distance

