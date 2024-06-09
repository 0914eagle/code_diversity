
def get_min_phone_calls(detectors):
    # Initialize variables
    min_calls = 0
    calls_made = 0
    detectors = sorted(detectors, key=lambda x: x[0])

    # Iterate through the detectors
    for i in range(len(detectors)):
        # Get the current detector's position and total calls
        pos, total_calls = detectors[i]

        # If the detector is not the first one, calculate the number of calls made since the previous detector
        if i > 0:
            prev_pos, prev_total_calls = detectors[i - 1]
            calls_made += prev_total_calls - prev_pos

        # Add the total calls made by the current detector
        calls_made += total_calls - pos

        # Update the minimum number of calls made
        min_calls = max(min_calls, calls_made)

    return min_calls

