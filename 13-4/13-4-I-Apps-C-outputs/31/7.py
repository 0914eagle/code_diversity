
def solve(detectors, houses):
    # Initialize a list to store the number of phone calls at each house
    calls = [0] * (houses + 1)

    # Loop through each detector and increment the number of phone calls at the corresponding house
    for detector in detectors:
        calls[detector[0]] += detector[1]
        calls[detector[0] + 1] += detector[1]

    # Return the minimum number of phone calls made
    return min(calls)

