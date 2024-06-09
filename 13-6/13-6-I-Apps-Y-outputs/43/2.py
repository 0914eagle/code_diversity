
def is_edward_right(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the interval starts after the current time, add the difference to the current time
        if interval[0] > current_time:
            current_time += interval[0] - current_time

        # If the interval ends after the current time, set the current time to the end of the interval
        if interval[1] > current_time:
            current_time = interval[1]

    # If the current time is greater than or equal to the total time, return "edward is right"
    if current_time >= sum(interval[1] for interval in intervals):
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    return "gunilla has a point"

