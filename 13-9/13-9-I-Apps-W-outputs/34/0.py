
def get_maximum_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Iterate from 1 to n
    for x in range(1, n + 1):
        # Check if x is a valid value of x
        if x <= M and n % x <= D * k:
            # Calculate the number of candies Arkady will receive
            candies = n // x
            # Update the maximum number of candies if necessary
            max_candies = max(max_candies, candies)
    # Return the maximum number of candies Arkady can receive
    return max_candies

