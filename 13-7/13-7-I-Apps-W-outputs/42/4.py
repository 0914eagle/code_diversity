
def get_min_time(n, x, v):
    # Sort the positions of the friends from south to north
    x.sort()
    
    # Initialize the minimum time needed to gather all the friends
    min_time = 0
    
    # Loop through each friend and calculate the time needed to gather them
    for i in range(n):
        # Calculate the distance between the current friend and the previous friend
        dist = x[i] - x[i-1] if i > 0 else x[i]
        
        # Calculate the time needed to cover the distance at the maximum speed
        time = dist / v[i]
        
        # Update the minimum time needed to gather all the friends
        min_time += time
    
    return min_time

