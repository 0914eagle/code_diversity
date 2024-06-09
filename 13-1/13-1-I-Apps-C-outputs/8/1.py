
def get_time(start, end, conveyors):
    # Calculate the distance between start and end
    distance = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5

    # Initialize the minimum time to travel the distance
    min_time = distance

    # Loop through each conveyor
    for conveyor in conveyors:
        # Calculate the distance to the start of the conveyor
        start_distance = ((conveyor[0] - start[0]) ** 2 + (conveyor[1] - start[1]) ** 2) ** 0.5

        # Calculate the distance to the end of the conveyor
        end_distance = ((conveyor[2] - end[0]) ** 2 + (conveyor[3] - end[1]) ** 2) ** 0.5

        # Calculate the total distance to travel on the conveyor
        conveyor_distance = start_distance + end_distance

        # Calculate the time to travel the conveyor distance
        conveyor_time = conveyor_distance / 2.0

        # Calculate the total time to travel the distance
        total_time = conveyor_time + min_time

        # Update the minimum time if necessary
        if total_time < min_time:
            min_time = total_time

    # Return the minimum time
    return min_time

