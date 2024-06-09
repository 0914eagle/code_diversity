
def solve(A, B, Q, s, t, x):
    # Sort the locations of the shrines and temples
    shrines = sorted(s)
    temples = sorted(t)
    
    # Initialize the answer array
    answer = [0] * Q
    
    # Loop through each query
    for i in range(Q):
        # Get the current query
        curr_x = x[i]
        
        # Find the closest shrine and temple to the current point
        shrine_index = find_closest(curr_x, shrines)
        temple_index = find_closest(curr_x, temples)
        
        # Calculate the distance to the closest shrine and temple
        shrine_dist = abs(curr_x - shrines[shrine_index])
        temple_dist = abs(curr_x - temples[temple_index])
        
        # Update the answer array
        answer[i] = min(shrine_dist + temple_dist, abs(shrine_dist - temple_dist))
    
    return answer

def find_closest(x, locations):
    # Find the index of the closest location to the current point
    for i in range(len(locations)):
        if locations[i] >= x:
            return i - 1
    return len(locations) - 1

