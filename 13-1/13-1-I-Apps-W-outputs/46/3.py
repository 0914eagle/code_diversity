
import math

def solve(n, r, x):
    # Initialize the y-coordinates of the disks
    y = [10**100 for i in range(n)]

    # Iterate through the disks and calculate their new positions
    for i in range(n):
        # Calculate the distance the disk has to move
        distance = y[i] - r

        # Calculate the new position of the disk
        y[i] = r + distance * math.cos(math.acos(r / distance))

    return y

