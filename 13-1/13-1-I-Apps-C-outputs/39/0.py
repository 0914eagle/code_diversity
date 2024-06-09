
def get_min_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles):
    # Calculate the distance from Adil's current position to each bottle
    distances = []
    for bottle in bottles:
        distances.append(((bottle[0] - adil_x) ** 2 + (bottle[1] - adil_y) ** 2) ** 0.5)
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Initialize the total distance as the distance from Adil's current position to the closest bottle
    total_distance = distances[0]
    
    # Loop through the distances and calculate the total distance
    for i in range(1, len(distances)):
        total_distance += distances[i]
    
    return total_distance

