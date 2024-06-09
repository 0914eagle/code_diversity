
def solve(ell, n):
    # Initialize the number of layers as 1
    k = 1
    # Loop until the roll runs out even though Nick still needs more paper
    while True:
        # Calculate the length of the roll after using n centimeters
        length = ell - n
        # If the length is greater than or equal to n, break the loop
        if length >= n:
            break
        # Increment the number of layers
        k += 1
        # Set the length to the original length
        length = ell
    return k

