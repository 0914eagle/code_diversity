
def solve(l, n):
    # Initialize the number of rolls as 1
    k = 1
    # Loop until the rolls are sufficient
    while l < n:
        # Increase the number of rolls by 1
        k += 1
        # Calculate the total length of the rolls
        l += l
    # Return the smallest number of rolls that are sufficient
    return k

