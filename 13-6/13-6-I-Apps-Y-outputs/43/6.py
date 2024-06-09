
def boiling_pot(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time and the previous start time
    current_time = 0
    previous_start = 0

    # Iterate through the intervals
    for start, end in intervals:
        # Update the current time
        current_time += end - start

        # If the current time is greater than the previous start time, it means the pot has started boiling
        if current_time > previous_start:
            return "edward is right"

        # Update the previous start time
        previous_start = start

    # If the loop completes and the pot has not started boiling, it means Gunilla has a point
    return "gunilla has a point"

