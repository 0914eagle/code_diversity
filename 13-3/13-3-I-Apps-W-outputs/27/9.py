
def solve(n, s, volumes):
    # Sort the volumes in descending order
    volumes.sort(reverse=True)
    # Initialize the sum of volumes to 0
    total = 0
    # Iterate through the volumes and add them to the sum
    for volume in volumes:
        total += volume
        # If the sum is greater than or equal to the desired volume, return the current volume
        if total >= s:
            return volume
    # If the sum is less than the desired volume, it is not possible to pour the desired amount of kvass, so return -1
    return -1

