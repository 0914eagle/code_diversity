
def solve(detectors, houses):
    # Initialize a list to store the minimum number of phone calls made at each house
    min_calls = [0] * (houses + 1)
    # Loop through each detector
    for detector in detectors:
        # Get the position and total number of phone calls detected by the detector
        position, calls = detector
        # Update the minimum number of phone calls made at the detector's position and the adjacent houses
        min_calls[position] += calls
        min_calls[position + 1] += calls
    # Return the sum of the minimum number of phone calls made at each house
    return sum(min_calls)

