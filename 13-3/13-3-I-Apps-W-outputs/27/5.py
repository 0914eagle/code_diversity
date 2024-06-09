
def solve(n, s, volumes):
    # Sort the volumes in descending order
    volumes.sort(reverse=True)
    # Initialize the sum of volumes to 0
    sum_volumes = 0
    # Iterate through the volumes and check if the sum is greater than or equal to s
    for i in range(n):
        sum_volumes += volumes[i]
        if sum_volumes >= s:
            return volumes[i]
    # If the sum is not greater than or equal to s, return -1
    return -1

