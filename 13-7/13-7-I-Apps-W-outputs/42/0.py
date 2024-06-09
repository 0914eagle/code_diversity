
def solve(n, x, v):
    # Calculate the maximum speed of each friend
    max_speed = [v[i] for i in range(n)]
    
    # Sort the friends by their current position
    sorted_x = sorted(x)
    
    # Initialize the minimum time needed to gather all friends
    min_time = 0
    
    # Iterate over the friends and calculate the time needed to gather them
    for i in range(n):
        # Calculate the distance between the current friend and the previous friend
        dist = abs(sorted_x[i] - sorted_x[i-1])
        
        # Calculate the time needed to cover the distance at the maximum speed
        time = dist / max_speed[i-1]
        
        # Add the time to the minimum time needed to gather all friends
        min_time += time
    
    return min_time

