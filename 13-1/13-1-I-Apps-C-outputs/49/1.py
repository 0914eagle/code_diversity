
def get_min_phone_calls(detectors):
    # Sort the detectors by their position
    sorted_detectors = sorted(detectors, key=lambda x: x[0])

    # Initialize the minimum number of phone calls to 0
    min_phone_calls = 0

    # Iterate through the detectors
    for i in range(len(sorted_detectors)):
        # Get the current detector's position and total number of phone calls
        pos, calls = sorted_detectors[i]

        # If this is the first detector, set the minimum number of phone calls to its total number of calls
        if i == 0:
            min_phone_calls = calls

        # If this is not the first detector, compare its total number of calls to the minimum number of phone calls
        else:
            # If the current detector's total number of calls is less than the minimum number of phone calls, update the minimum number of phone calls
            if calls < min_phone_calls:
                min_phone_calls = calls

    # Return the minimum number of phone calls
    return min_phone_calls

