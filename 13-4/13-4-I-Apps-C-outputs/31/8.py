
def solve(detectors, houses):
    # Initialize a list to store the number of phone calls at each house
    calls = [0] * (houses + 1)

    # Iterate over the detectors and update the number of phone calls at each house
    for detector in detectors:
        position, total_calls = detector
        calls[position] += total_calls
        calls[position + 1] += total_calls

    # Find the minimum number of phone calls made
    min_calls = min(calls)

    # Return the minimum number of phone calls made
    return min_calls

