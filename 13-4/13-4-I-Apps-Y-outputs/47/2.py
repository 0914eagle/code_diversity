
def get_k(l, n):
    # Initialize k as 1
    k = 1
    # Loop until k is found
    while True:
        # Calculate the length of the rolls
        roll_length = l * k
        # Check if the roll length is greater than or equal to the number of centimeters needed
        if roll_length >= n:
            # If it is, return k
            return k
        # Increment k by 1
        k += 1

