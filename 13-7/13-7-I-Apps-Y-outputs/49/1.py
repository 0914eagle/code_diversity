
def can_atcodeer_travel(plan):
    # Sort the plan by time
    plan.sort(key=lambda x: x[0])
    # Initialize the current position and time
    current_position = (0, 0)
    current_time = 0
    # Iterate through the plan
    for i in range(len(plan)):
        # Get the next event
        next_event = plan[i]
        # Check if the event is valid
        if next_event[0] != current_time + 1:
            return "No"
        # Update the current position and time
        current_position = (next_event[1], next_event[2])
        current_time = next_event[0]
    # Check if AtCoDeer reached his destination
    if current_position != (1, 1):
        return "No"
    # AtCoDeer can carry out his plan
    return "Yes"

