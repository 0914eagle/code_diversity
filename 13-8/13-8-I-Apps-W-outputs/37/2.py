
def solve(A, B, Q, shrine_distances, temple_distances, starting_points):
    # Sort the shrine and temple distances
    shrine_distances.sort()
    temple_distances.sort()
    
    # Initialize the minimum distance dictionary
    min_distance = {}
    
    # Loop through each query
    for i in range(Q):
        # Get the starting point and calculate the minimum distance
        starting_point = starting_points[i]
        min_distance[i] = min(abs(starting_point - shrine_distances[0]), abs(starting_point - temple_distances[0]))
        
        # Loop through each shrine and temple
        for j in range(1, A):
            for k in range(1, B):
                # Calculate the distance to visit both the shrine and the temple
                distance_to_shrine = abs(starting_point - shrine_distances[j])
                distance_to_temple = abs(starting_point - temple_distances[k])
                
                # Check if the current distance is less than the minimum distance
                if distance_to_shrine + distance_to_temple < min_distance[i]:
                    min_distance[i] = distance_to_shrine + distance_to_temple
    
    # Return the minimum distances
    return [min_distance[i] for i in range(Q)]

