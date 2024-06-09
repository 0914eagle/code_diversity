
def solve(detectors, houses):
    # Initialize a list to store the number of phone calls detected by each detector
    calls = [0] * len(detectors)
    
    # Iterate over the detectors
    for i, detector in enumerate(detectors):
        # Get the position of the detector and the total number of phone calls detected
        position, total_calls = detector
        
        # Update the number of phone calls detected by the detector
        calls[i] = total_calls
        
        # If the detector is not on the east-west border, update the number of phone calls detected by the neighboring detector
        if position > 1 and position < houses:
            calls[(i + 1) % len(detectors)] += total_calls
    
    # Return the minimum number of phone calls detected by any detector
    return min(calls)

