
def get_k(l, n):
    # Initialize k to 1
    k = 1
    # Loop until the condition is met
    while True:
        # Calculate the total length of the rolls
        total_length = l * k
        # Check if the total length is greater than or equal to the number of centimeters needed
        if total_length >= n:
            # If it is, return k
            return k
        # If it is not, increment k and try again
        k += 1

