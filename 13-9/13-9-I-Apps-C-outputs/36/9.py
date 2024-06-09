
def solve(coords, conveyors):
    # Initialize the minimum time to infinite
    min_time = float('inf')
    
    # Loop through all possible combinations of conveyors
    for combination in itertools.product([0, 1], repeat=len(conveyors)):
        # Initialize the current time to 0
        current_time = 0
        
        # Loop through all the conveyors
        for i, conveyor in enumerate(conveyors):
            # If the passenger is on the conveyor, move at the conveyor speed
            if combination[i] == 1:
                current_time += conveyor[2] - conveyor[0]
            # If the passenger is on the floor, move at the floor speed
            else:
                current_time += coords[i+1] - conveyor[i]
        
        # If the current time is less than the minimum time, update the minimum time
        if current_time < min_time:
            min_time = current_time
    
    # Return the minimum time
    return min_time

