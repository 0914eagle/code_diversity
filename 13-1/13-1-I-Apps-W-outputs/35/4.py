
def get_min_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance as the distance between the first two vehicles
    min_distance = abs(vehicles[1][0] - vehicles[0][0])
    
    # Loop through the vehicles and calculate the minimum distance between any two vehicles
    for i in range(1, len(vehicles) - 1):
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        if distance < min_distance:
            min_distance = distance
    
    return min_distance

