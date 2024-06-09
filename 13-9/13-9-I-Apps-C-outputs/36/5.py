
def solve(A, B, conveyors):
    # Find the shortest distance between A and B
    dist = ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5
    
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Loop through all possible combinations of conveyors
    for i in range(len(conveyors)+1):
        # Calculate the time it takes to travel along the conveyors
        time = 0
        for j in range(i):
            time += ((conveyors[j][2]-conveyors[j][0])**2 + (conveyors[j][3]-conveyors[j][1])**2)**0.5
        
        # Calculate the time it takes to travel along the floor
        time += dist
        
        # Update the minimum time if necessary
        if time < min_time:
            min_time = time
    
    # Return the minimum time
    return min_time

