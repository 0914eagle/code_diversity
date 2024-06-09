
def get_max_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x from 1 to M
    for x in range(1, M + 1):
        # Calculate the number of candies that each person will receive
        candies_per_person = x
        # Calculate the number of complete cycles that can be done with the given x
        complete_cycles = n // (k * x)
        # Calculate the number of leftover candies
        leftover_candies = n % (k * x)
        # Calculate the number of candies that each person will receive in the last cycle
        last_cycle_candies = leftover_candies // k
        # Calculate the total number of candies received by each person
        total_candies = (complete_cycles * k * candies_per_person) + last_cycle_candies
        # Check if the total number of candies received by each person is less than or equal to D
        if total_candies <= D:
            # Update the maximum number of candies if the total number of candies received is greater than the current maximum
            max_candies = max(max_candies, total_candies)
    # Return the maximum number of candies that Arkady can receive
    return max_candies

