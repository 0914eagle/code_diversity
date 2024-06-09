
def solve(detectors, houses):
    # Initialize a list to store the number of calls made by each detector
    calls = [0] * len(detectors)
    
    # Iterate over each detector
    for i, detector in enumerate(detectors):
        # Get the position of the detector and the total number of calls detected
        position, total_calls = detector
        
        # Iterate over the houses between the detector position and the next house
        for j in range(position, houses):
            # If the detector is on the eastward side of the house, add the total number of calls detected to the number of calls made by the detector
            if j == position:
                calls[i] += total_calls
            # If the detector is on the westward side of the house, subtract the total number of calls detected from the number of calls made by the detector
            elif j == position + 1:
                calls[i] -= total_calls
    
    # Return the minimum number of calls made by any detector
    return min(calls)

