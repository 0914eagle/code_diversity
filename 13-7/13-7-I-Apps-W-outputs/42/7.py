
def get_min_time(n, x, v):
    # Sort the positions of the friends from south to north
    x.sort()
    
    # Initialize the minimum time needed to gather all the friends
    min_time = 0
    
    # Iterate over the friends and calculate the time needed for each friend to reach the meeting point
    for i in range(n):
        # Calculate the distance between the current friend and the meeting point
        distance = abs(x[i] - x[0])
        
        # Calculate the time needed for the friend to reach the meeting point
        time = distance / v[i]
        
        # Update the minimum time needed to gather all the friends
        min_time += time
    
    return min_time

