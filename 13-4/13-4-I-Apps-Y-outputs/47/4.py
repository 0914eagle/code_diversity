
def solve(ell, n):
    # Initialize the number of rolls as 1
    k = 1
    # Loop until the input condition is met
    while True:
        # Calculate the length of the regular roll
        regular_roll_length = ell * k
        # Calculate the length of the backup rolls
        backup_roll_length = regular_roll_length * (k - 1)
        # Check if the input condition is met
        if regular_roll_length + backup_roll_length >= n:
            break
        # Increment the number of rolls
        k += 1
    return k

