
def can_atcodeer_carry_out_his_plan(plan):
    # Sort the plan by time
    sorted_plan = sorted(plan, key=lambda x: x[0])

    # Initialize the current position and time
    current_position = (0, 0)
    current_time = 0

    # Iterate through the plan and check if AtCoDeer can reach each destination
    for i in range(len(sorted_plan)):
        destination = sorted_plan[i][1:]
        if destination != current_position:
            # Calculate the distance between the current position and the destination
            dx = abs(destination[0] - current_position[0])
            dy = abs(destination[1] - current_position[1])

            # Check if the distance is valid
            if dx > 1 or dy > 1:
                return "No"

        # Update the current position and time
        current_position = destination
        current_time = sorted_plan[i][0]

    return "Yes"

