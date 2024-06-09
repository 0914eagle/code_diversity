
def solve(A, B, Q, shrine_locations, temple_locations, x):
    # Sort the shrine and temple locations
    shrine_locations.sort()
    temple_locations.sort()
    
    # Initialize the minimum distance to visit one shrine and one temple
    min_distance = float('inf')
    
    # Loop through each query
    for i in range(Q):
        # Get the current query
        current_x = x[i]
        
        # Initialize the minimum distance for this query
        min_distance_query = float('inf')
        
        # Loop through each shrine and temple
        for j in range(A):
            for k in range(B):
                # Calculate the distance to visit this shrine and temple
                distance = abs(current_x - shrine_locations[j]) + abs(current_x - temple_locations[k])
                
                # Check if this is the minimum distance so far
                if distance < min_distance_query:
                    min_distance_query = distance
        
        # Add the minimum distance for this query to the total minimum distance
        min_distance += min_distance_query
    
    return min_distance

