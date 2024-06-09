
def is_pot_boiling_at_same_time(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is within the interval, the pot is boiling
        if current_time >= interval[0] and current_time <= interval[1]:
            return "edward is right"
        # Otherwise, increment the current time by the length of the interval
        current_time += (interval[1] - interval[0])

    # If the pot has not boiled by the end of the last interval, Gunilla has a point
    return "gunilla has a point"

