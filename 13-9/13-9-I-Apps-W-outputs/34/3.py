
def get_max_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        candies_per_person = x
        # Calculate the number of full cycles
        num_cycles = n // x
        # Calculate the number of candies given in the last cycle
        last_cycle = n % x
        # Calculate the total number of candies given
        total_candies = (num_cycles * candies_per_person) + last_cycle
        # Check if the total number of candies is divisible by k
        if total_candies % k == 0:
            # Calculate the maximum number of candies given to each person
            max_candies_per_person = total_candies // k
            # Check if the maximum number of candies given to each person is less than or equal to D
            if max_candies_per_person <= D:
                # Update the maximum number of candies
                max_candies = max(max_candies, total_candies)
    # Return the maximum number of candies
    return max_candies

