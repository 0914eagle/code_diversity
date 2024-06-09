
def solve(l, n):
    # Initialize the number of rolls as 1
    k = 1
    # Loop until the number of rolls is greater than or equal to the input l
    while l > 0:
        # Calculate the remaining length of the roll
        l = l - n
        # If the remaining length is negative, increase the number of rolls
        if l < 0:
            k += 1
            # Reset the remaining length to the input l
            l = l + n
    return k

