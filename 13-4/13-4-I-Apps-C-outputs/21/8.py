
def find_min_time(x1, y1, x2, y2, v_max, t, wind):
    # Calculate the distance between the two points
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    # Initialize the minimum time to be the distance divided by the maximum speed
    min_time = distance / v_max
    
    # Iterate through the wind data
    for i in range(t):
        # Calculate the time it takes to travel the distance in the current wind
        time = distance / wind[i][0]
        
        # If the time is less than the minimum time, update the minimum time
        if time < min_time:
            min_time = time
    
    # Return the minimum time
    return min_time

