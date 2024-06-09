
def solve(n, x, v):
    # Sort the positions of the friends from south to north
    x.sort()
    
    # Initialize the minimum time needed to gather all the friends
    time = 0
    
    # Iterate over the friends
    for i in range(n):
        # Calculate the distance between the current friend and the previous friend
        dist = x[i] - x[i-1]
        
        # Calculate the time needed to cover the distance at the maximum speed
        time += dist / v[i]
    
    return time

