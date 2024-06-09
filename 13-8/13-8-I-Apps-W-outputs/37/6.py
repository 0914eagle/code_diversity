
def solve(A, B, Q, shrine_locations, temple_locations, x):
    # Sort the shrine and temple locations
    shrine_locations.sort()
    temple_locations.sort()
    
    # Initialize the minimum distance variable
    min_distance = float('inf')
    
    # Loop through each query
    for i in range(Q):
        # Get the current query point
        current_point = x[i]
        
        # Initialize the minimum distance for this query
        min_distance_query = float('inf')
        
        # Loop through each shrine and temple
        for j in range(A):
            for k in range(B):
                # Calculate the distance to the current shrine and temple
                distance_shrine = abs(current_point - shrine_locations[j])
                distance_temple = abs(current_point - temple_locations[k])
                
                # Calculate the total distance to visit both the shrine and temple
                total_distance = distance_shrine + distance_temple
                
                # If the total distance is less than the current minimum distance, update the minimum distance
                if total_distance < min_distance_query:
                    min_distance_query = total_distance
                    
        # Add the minimum distance for this query to the total minimum distance
        min_distance += min_distance_query
    
    # Return the total minimum distance
    return min_distance

