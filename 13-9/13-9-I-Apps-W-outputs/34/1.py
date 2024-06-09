
def find_maximum_candies(n, k, M, D):
    # Initialize the maximum number of candies to 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies given to each person
        candies_per_person = x
        # Calculate the number of times each person receives candies
        num_times_person_receives_candies = n // (k * candies_per_person)
        # Calculate the number of candies received by Arkady
        candies_received_by_arkady = num_times_person_receives_candies * candies_per_person
        # Check if the number of candies received by Arkady is greater than the current maximum
        if candies_received_by_arkady > max_candies:
            # Update the maximum number of candies
            max_candies = candies_received_by_arkady
    # Return the maximum number of candies
    return max_candies

