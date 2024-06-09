
def get_min_phone_calls(detectors):
    # Sort the detectors by their position
    sorted_detectors = sorted(detectors, key=lambda x: x[0])

    # Initialize the minimum number of phone calls to 0
    min_calls = 0

    # Iterate through the detectors
    for i in range(len(sorted_detectors)):
        # Get the current detector's position and total number of calls
        pos, calls = sorted_detectors[i]

        # If this is the first detector, set the minimum number of calls to its total number of calls
        if i == 0:
            min_calls = calls

        # If this is not the first detector, compare its total number of calls to the minimum number of calls so far
        else:
            # Get the previous detector's position and total number of calls
            prev_pos, prev_calls = sorted_detectors[i - 1]

            # If the current detector is between the previous detector and the current detector, update the minimum number of calls
            if prev_pos < pos <= prev_pos + prev_calls:
                min_calls = min(min_calls, calls + prev_calls)

    return min_calls

