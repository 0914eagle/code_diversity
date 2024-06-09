
def is_pot_boiling_at_same_time(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize variables to keep track of the current time and the last time the pot was seen boiling
    current_time = 0
    last_boiling_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is within the interval, the pot was not being watched
        if current_time >= interval[0] and current_time <= interval[1]:
            continue

        # If the current time is after the interval and the pot was seen boiling, update the last boiling time
        if current_time > interval[1] and last_boiling_time == 0:
            last_boiling_time = current_time

        # Increment the current time by the length of the interval
        current_time += interval[1] - interval[0]

    # If the last boiling time is still 0, it means the pot was never seen boiling
    if last_boiling_time == 0:
        return "edward is right"

    # If the last boiling time is not 0, it means the pot was seen boiling at least once
    return "gunilla has a point"

