
def get_fastest_time(start, end, conveyors):
    # Initialize the minimum time to get from start to end as the straight-line distance between the two points
    min_time = abs(end[0] - start[0]) + abs(end[1] - start[1])

    # Loop through each conveyor
    for conveyor in conveyors:
        # Check if the start point is on the conveyor
        if start in conveyor:
            # Get the index of the start point on the conveyor
            start_index = conveyor.index(start)
            # Check if the end point is on the conveyor
            if end in conveyor:
                # Get the index of the end point on the conveyor
                end_index = conveyor.index(end)
                # Calculate the time to travel on the conveyor from start to end
                conveyor_time = abs(end_index - start_index) / 2
                # Check if the time to travel on the conveyor is faster than the minimum time
                if conveyor_time < min_time:
                    # Update the minimum time
                    min_time = conveyor_time
            # Check if the end point is not on the conveyor
            else:
                # Calculate the time to travel on the conveyor from start to the end point that is closest to the conveyor
                conveyor_time = abs(conveyor.index(closest_point_on_conveyor(end, conveyor)) - start_index) / 2
                # Check if the time to travel on the conveyor is faster than the minimum time
                if conveyor_time < min_time:
                    # Update the minimum time
                    min_time = conveyor_time
        # Check if the end point is on the conveyor
        elif end in conveyor:
            # Get the index of the end point on the conveyor
            end_index = conveyor.index(end)
            # Calculate the time to travel on the conveyor from the start point that is closest to the conveyor to end
            conveyor_time = abs(end_index - conveyor.index(closest_point_on_conveyor(start, conveyor))) / 2
            # Check if the time to travel on the conveyor is faster than the minimum time
            if conveyor_time < min_time:
                # Update the minimum time
                min_time = conveyor_time

    # Return the minimum time
    return min_time

# Find the point on a conveyor that is closest to a given point
def closest_point_on_conveyor(point, conveyor):
    # Initialize the closest point as the first point on the conveyor
    closest_point = conveyor[0]
    # Initialize the minimum distance as the distance between the closest point and the given point
    min_distance = abs(closest_point[0] - point[0]) + abs(closest_point[1] - point[1])

    # Loop through each point on the conveyor
    for i in range(1, len(conveyor)):
        # Calculate the distance between the current point and the given point
        distance = abs(conveyor[i][0] - point[0]) + abs(conveyor[i][1] - point[1])
        # Check if the distance is smaller than the minimum distance
        if distance < min_distance:
            # Update the closest point and the minimum distance
            closest_point = conveyor[i]
            min_distance = distance

    # Return the closest point on the conveyor
    return closest_point

