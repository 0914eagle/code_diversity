
def get_maximum_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        num_candies = x * (k - 1)
        # Calculate the number of candies received by Arkady
        arkady_candies = n - num_candies
        # Check if the number of candies received by Arkady is divisible by D
        if arkady_candies % D == 0:
            # If it is divisible, update the maximum number of candies
            max_candies = max(max_candies, arkady_candies)
    # Return the maximum number of candies
    return max_candies

