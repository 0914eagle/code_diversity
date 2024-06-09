
def solve(A, B, Q, s, t, x):
    # Sort the shrines and temples by their distances from the west end of the road
    shrines = sorted(s)
    temples = sorted(t)
    
    # Initialize the answer array
    answers = [0] * Q
    
    # Iterate over each query
    for i in range(Q):
        # Get the current query
        curr_x = x[i]
        
        # Initialize the minimum distance to visit one shrine and one temple
        min_dist = float('inf')
        
        # Iterate over each shrine and temple
        for j in range(A):
            for k in range(B):
                # Calculate the distance to visit the j-th shrine and k-th temple
                dist = abs(curr_x - shrines[j]) + abs(curr_x - temples[k])
                
                # Update the minimum distance if necessary
                if dist < min_dist:
                    min_dist = dist
        
        # Add the minimum distance to the answer array
        answers[i] = min_dist
    
    return answers

