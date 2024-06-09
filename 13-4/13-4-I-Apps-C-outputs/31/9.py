
def solve(N, M, detectors):
    # Initialize a list to store the minimum number of phone calls made at each position
    min_calls = [0] * (M + 1)
    # Loop through each detector
    for detector in detectors:
        # Get the position and total number of phone calls detected by the detector
        position, total_calls = detector
        # Loop through each position between the detector position and the end of the street
        for i in range(position, M + 1):
            # Add the total number of phone calls detected by the detector to the minimum number of phone calls made at that position
            min_calls[i] += total_calls
    # Return the maximum value in the min_calls list, which is the minimal number of phone calls made
    return max(min_calls)

