
def is_edward_right(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize variables to keep track of the current boiling time and the previous boiling time
    current_time = 0
    previous_time = 0

    # Loop through each interval
    for interval in intervals:
        # If the interval starts before the current boiling time, it means the pot has already boiled
        if interval[0] < current_time:
            return "gunilla has a point"

        # If the interval starts after the current boiling time, it means the pot has not yet boiled
        if interval[0] > current_time:
            current_time = interval[1]

        # If the interval ends after the current boiling time, it means the pot has not yet boiled
        if interval[1] > current_time:
            current_time = interval[1]

    # If we have reached the end of the intervals and the pot has not yet boiled, it means Edward is right
    return "edward is right"

