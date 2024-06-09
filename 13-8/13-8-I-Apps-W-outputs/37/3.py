
def solve(A, B, Q, s, t, x):
    # Sort the shrines and temples by their distances from the west end of the road
    shrines = sorted(s)
    temples = sorted(t)
    
    # Initialize the answer array
    answer = []
    
    # Loop through each query
    for i in range(Q):
        # Get the starting point for this query
        start = x[i]
        
        # Initialize the minimum distance to visit one shrine and one temple
        min_dist = float('inf')
        
        # Loop through each shrine and temple
        for j in range(A):
            for k in range(B):
                # Get the distance to visit this shrine and temple
                dist = abs(shrines[j] - temples[k])
                
                # If the distance is less than the minimum distance, update the minimum distance
                if dist < min_dist:
                    min_dist = dist
        
        # Add the minimum distance to the answer array
        answer.append(min_dist)
    
    return answer

