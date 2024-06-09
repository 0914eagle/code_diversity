
def get_max_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Check if x is a valid value of x
        if n % x == 0 and n // x <= k and n // x >= D:
            # Calculate the number of candies Arkady can receive
            candies = n // x
            # Update the maximum number of candies if necessary
            max_candies = max(max_candies, candies)
    # Return the maximum number of candies Arkady can receive
    return max_candies

