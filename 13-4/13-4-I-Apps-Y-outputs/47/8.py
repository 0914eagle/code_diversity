
def solve(ell, n):
    # Initialize the number of rolls as 1
    k = 1
    # Loop until the crisis is guaranteed to never happen
    while True:
        # Calculate the length of the regular roll
        regular_roll_length = ell - (k - 1) * ell
        # Check if the crisis can happen with the current number of rolls
        if regular_roll_length < n:
            # Increase the number of rolls and try again
            k += 1
        else:
            # The crisis will never happen with the current number of rolls, so break the loop
            break
    return k

