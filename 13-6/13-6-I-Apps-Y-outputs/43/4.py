
def solve(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is less than the start time of the interval, move the current time to the start time of the interval
        if current_time < interval[0]:
            current_time = interval[0]

        # If the current time is greater than the end time of the interval, move the current time to the end time of the interval
        if current_time > interval[1]:
            current_time = interval[1]

    # If the current time is equal to the end time of the last interval, return "edward is right"
    if current_time == intervals[-1][1]:
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    return "gunilla has a point"

