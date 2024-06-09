
def get_max_candies(n, k, M, D):
    # Initialize the maximum number of candies to 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        num_candies = x * (k - 1)
        # Calculate the number of candies left over
        leftover = n - num_candies
        # Check if the number of candies left over is divisible by x
        if leftover % x == 0:
            # Calculate the number of candies received by each person
            num_candies_each = num_candies // k
            # Check if the number of candies received by each person is less than or equal to D
            if num_candies_each <= D:
                # Update the maximum number of candies if necessary
                max_candies = max(max_candies, num_candies_each)
    # Return the maximum number of candies
    return max_candies

