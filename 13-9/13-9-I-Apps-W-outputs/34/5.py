
def solve(n, k, M, D):
    # Initialize the maximum number of candies that Arkady can receive
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, M + 1):
        # Calculate the number of candies that each person will receive
        candies_per_person = x
        # Calculate the number of times each person will receive candies
        num_times_each_person_receives = int(n / candies_per_person)
        # Calculate the number of candies that will be thrown away
        num_candies_thrown_away = n % candies_per_person
        # Check if the number of candies thrown away is less than or equal to the maximum number of times each person can receive candies
        if num_candies_thrown_away <= D:
            # Calculate the total number of candies that Arkady can receive
            total_candies = candies_per_person * num_times_each_person_receives
            # Update the maximum number of candies that Arkady can receive
            max_candies = max(max_candies, total_candies)
    # Return the maximum number of candies that Arkady can receive
    return max_candies

