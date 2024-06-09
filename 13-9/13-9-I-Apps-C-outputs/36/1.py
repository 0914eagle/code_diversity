
def get_time(start, end, conveyors):
    # Calculate the distance between start and end points
    distance = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5

    # Initialize the minimum time to travel the distance
    min_time = distance / 1

    # Iterate over each conveyor
    for conveyor in conveyors:
        # Calculate the distance to the conveyor
        conveyor_distance = ((conveyor[0] - start[0]) ** 2 + (conveyor[1] - start[1]) ** 2) ** 0.5

        # Calculate the time to travel the distance to the conveyor
        conveyor_time = conveyor_distance / 2

        # Calculate the distance from the conveyor to the end point
        end_distance = ((end[0] - conveyor[2]) ** 2 + (end[1] - conveyor[3]) ** 2) ** 0.5

        # Calculate the time to travel the distance from the conveyor to the end point
        end_time = end_distance / 1

        # Calculate the total time to travel from start to end using the conveyor
        total_time = conveyor_time + end_time

        # Update the minimum time if the total time is less than the current minimum time
        if total_time < min_time:
            min_time = total_time

    return min_time

