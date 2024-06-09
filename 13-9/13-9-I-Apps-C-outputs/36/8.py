
def get_fastest_time(start, end, conveyors):
    # Initialize the minimum time to travel from start to end
    min_time = 0

    # Loop through each conveyor
    for conveyor in conveyors:
        # Get the start and end points of the conveyor
        start_point = conveyor[0]
        end_point = conveyor[1]

        # Check if the start point is on the conveyor
        if start_point[0] == start[0] and start_point[1] == start[1]:
            # Calculate the time it takes to travel from the start point to the end point on the conveyor
            conveyor_time = (end_point[0] - start_point[0]) / 2

            # Check if the end point is also on the conveyor
            if end_point[0] == end[0] and end_point[1] == end[1]:
                # If the end point is also on the conveyor, calculate the total time it takes to travel from the start to the end on the conveyor
                total_time = conveyor_time + min_time
            else:
                # If the end point is not on the conveyor, calculate the time it takes to travel from the start point to the end point on the conveyor and the time it takes to travel from the end point to the end on the floor
                total_time = conveyor_time + (end[0] - end_point[0]) + min_time

            # Update the minimum time if the total time is less than the current minimum time
            if total_time < min_time or min_time == 0:
                min_time = total_time

    # Return the minimum time it takes to travel from start to end
    return min_time

