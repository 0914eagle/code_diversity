
def solve(A, B, Q, s, t, x):
    # Sort the distances of the shrines and temples
    shrines = sorted(s)
    temples = sorted(t)
    
    # Initialize the answer array
    answer = []
    
    # Loop through each query
    for i in range(Q):
        # Find the closest shrine and temple to the starting point
        shrine = next((i for i in shrines if i <= x[i]), float('inf'))
        temple = next((i for i in temples if i <= x[i]), float('inf'))
        
        # Calculate the minimum distance to travel
        distance = abs(shrine - temple)
        
        # Add the answer to the array
        answer.append(distance)
    
    return answer

