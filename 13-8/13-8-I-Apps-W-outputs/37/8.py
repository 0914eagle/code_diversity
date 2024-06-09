
def solve(A, B, Q, shrine_locations, temple_locations, x_coordinates):
    # Sort the shrine and temple locations
    shrine_locations.sort()
    temple_locations.sort()
    
    # Initialize the answer array
    answers = [0] * Q
    
    # Loop through each query
    for i in range(Q):
        # Get the current query
        x = x_coordinates[i]
        
        # Find the closest shrine and temple to the current point
        shrine_index = bisect_left(shrine_locations, x)
        temple_index = bisect_left(temple_locations, x)
        
        # Calculate the distance to the closest shrine and temple
        shrine_distance = abs(shrine_locations[shrine_index] - x)
        temple_distance = abs(temple_locations[temple_index] - x)
        
        # Calculate the minimum distance to visit one shrine and one temple
        answers[i] = min(shrine_distance + temple_distance, abs(x - shrine_locations[0]) + abs(x - temple_locations[0]))
    
    return answers

