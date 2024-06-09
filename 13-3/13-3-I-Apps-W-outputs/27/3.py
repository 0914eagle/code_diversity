
def solve(n, s, volumes):
    # Sort the volumes in descending order
    volumes.sort(reverse=True)
    # Initialize the sum of volumes to 0
    total = 0
    # Iterate through the volumes and add them to the sum
    for v in volumes:
        total += v
        # If the sum is greater than or equal to the desired volume, return the current volume
        if total >= s:
            return v
    # If we reach this point, it means we couldn't find a combination that adds up to the desired volume, so return -1
    return -1

