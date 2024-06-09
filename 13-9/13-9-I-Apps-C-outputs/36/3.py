
def get_travel_time(start, end, conveyors):
    # Initialize the minimum travel time to infinity
    min_time = float('inf')
    
    # Iterate over all possible starting positions on the conveyors
    for start_pos in conveyors:
        # Calculate the distance from the starting position to the end position
        dist = abs(end[0] - start_pos[0]) + abs(end[1] - start_pos[1])
        
        # Calculate the time it takes to walk from the starting position to the end position
        time = dist / 1
        
        # If the time is less than the minimum time, update the minimum time
        if time < min_time:
            min_time = time
    
    # Return the minimum time
    return min_time

