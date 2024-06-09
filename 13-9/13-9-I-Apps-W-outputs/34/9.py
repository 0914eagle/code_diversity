
def find_maximum_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        num_candies = x * (k - 1)
        # Calculate the number of candies received by Arkady
        arkady_candies = x
        # Check if the number of candies received by Arkady is greater than the maximum
        if arkady_candies > max_candies:
            # Update the maximum number of candies
            max_candies = arkady_candies
    return max_candies

