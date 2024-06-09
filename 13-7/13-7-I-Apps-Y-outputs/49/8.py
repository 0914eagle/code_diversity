
def can_atcodeer_travel(plan):
    
    # Initialize the current position and time
    current_position = (0, 0)
    current_time = 0
    
    # Iterate through the plan
    for i in range(len(plan)):
        # Get the next point and time from the plan
        next_position = plan[i]
        next_time = next_position[0]
        
        # Check if AtCoDeer can travel to the next point at the next time
        if next_time > current_time + 1:
            return "No"
        if next_position != (current_position[0] + 1, current_position[1]) and \
           next_position != (current_position[0] - 1, current_position[1]) and \
           next_position != (current_position[0], current_position[1] + 1) and \
           next_position != (current_position[0], current_position[1] - 1):
            return "No"
        
        # Update the current position and time
        current_position = next_position
        current_time = next_time
    
    # If AtCoDeer can travel to all points, return "Yes"
    return "Yes"

