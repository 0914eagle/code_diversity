
def get_fastest_time(start, end, conveyors):
    # Initialize the fastest time to infinity
    fastest_time = float('inf')
    
    # Iterate over all possible combinations of walking on conveyors
    for conveyor_combination in itertools.product([False, True], repeat=len(conveyors)):
        # Initialize the current position and time
        current_position = start
        current_time = 0
        
        # Iterate over the conveyors and determine whether to walk on them or not
        for i, (conveyor, walk_on_conveyor) in enumerate(zip(conveyors, conveyor_combination)):
            # If we are not walking on the conveyor, just walk on the floor
            if not walk_on_conveyor:
                distance = np.linalg.norm(current_position - conveyor[0])
                current_position = conveyor[0]
                current_time += distance
            
            # If we are walking on the conveyor, walk the entire length of the conveyor
            else:
                distance = np.linalg.norm(conveyor[1] - conveyor[0])
                current_position = conveyor[1]
                current_time += distance
        
        # Add the time it takes to walk from the last conveyor to the end
        distance = np.linalg.norm(current_position - end)
        current_time += distance
        
        # Update the fastest time if the current time is faster than the previous fastest time
        if current_time < fastest_time:
            fastest_time = current_time
    
    return fastest_time

