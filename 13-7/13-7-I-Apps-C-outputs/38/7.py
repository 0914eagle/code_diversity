
def solve(detectors, houses):
    # Initialize a list to store the number of phone calls detected by each detector
    calls = [0] * len(detectors)
    
    # Loop through each detector
    for i in range(len(detectors)):
        # Get the position of the detector and the total number of phone calls detected
        position, total_calls = detectors[i]
        
        # Loop through each house
        for j in range(houses):
            # If the house is between the detector position and the next house, add the total number of phone calls detected to the list
            if position < j < position + 1:
                calls[i] += total_calls
    
    # Return the minimum number of phone calls detected by any detector
    return min(calls)

