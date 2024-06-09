
def solve(n, s, volumes):
    # Sort the volumes in descending order
    volumes.sort(reverse=True)
    # Initialize the sum of the volumes
    total = 0
    # Iterate through the volumes
    for i in range(n):
        # Check if the current volume is less than or equal to the target volume
        if volumes[i] <= s:
            # Add the current volume to the total
            total += volumes[i]
            # Subtract the current volume from the target volume
            s -= volumes[i]
        else:
            # If the current volume is greater than the target volume, break the loop
            break
    # Check if the total is greater than or equal to the target volume
    if total < s:
        # If not, return -1
        return -1
    else:
        # If so, return the least keg volume
        return volumes[0]

