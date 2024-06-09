
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest distance from each fragment to the assembly node
    distances = {}
    
    # Initialize the assembly node with the smallest possible distance (0)
    distances[1] = 0
    
    # Loop through each fragment
    for i in range(n):
        # Get the current fragment's location
        current_location = k[i]
        
        # Loop through all possible locations that the fragment could be at
        for location in range(1, current_location + 1):
            # If the fragment is not already at the assembly node
            if location != 1:
                # Get the distance from the current location to the assembly node
                distance = abs(location - 1)
                
                # If the distance is shorter than the current shortest distance, update the dictionary
                if distance < distances.get(location, float('inf')):
                    distances[location] = distance
    
    # Return the sum of the shortest distances from each fragment to the assembly node
    return sum(distances.values())

