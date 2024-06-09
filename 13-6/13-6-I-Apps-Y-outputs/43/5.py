
def is_edward_right(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current boiling time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the interval starts after the current time, update the current time
        if interval[0] > current_time:
            current_time = interval[0]

        # If the interval ends after the current time, update the current time
        if interval[1] > current_time:
            current_time = interval[1]

    # If the current time is equal to the maximum time in all intervals, Edward is right
    if current_time == max(interval[1] for interval in intervals):
        return "edward is right"

    # Otherwise, Gunilla has a point
    return "gunilla has a point"

