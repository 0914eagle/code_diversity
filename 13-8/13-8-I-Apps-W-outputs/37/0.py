
def solve(A, B, Q, shrine_distances, temple_distances, starting_points):
    # Sort the shrine and temple distances from west to east
    shrine_distances.sort()
    temple_distances.sort()
    
    # Initialize the minimum distance to visit one shrine and one temple as infinity
    min_distance = float('inf')
    
    # Loop through each query
    for i in range(Q):
        # Get the starting point for the ith query
        start = starting_points[i]
        
        # Initialize the minimum distance for the ith query as infinity
        min_distance_query = float('inf')
        
        # Loop through each shrine and temple from west to east
        for j in range(A):
            for k in range(B):
                # Calculate the distance to visit the jth shrine and kth temple
                distance = abs(start - shrine_distances[j]) + abs(start - temple_distances[k])
                
                # If the distance is less than the minimum distance, update the minimum distance
                if distance < min_distance_query:
                    min_distance_query = distance
                    
        # Add the minimum distance for the ith query to the total minimum distance
        min_distance += min_distance_query
    
    return min_distance

