
def solve(N, M, food_times):
    # Initialize the minimum total waiting time to infinity
    min_wait_time = float('inf')
    # Loop through all possible combinations of feeding bowls
    for combination in itertools.combinations(range(M), N):
        # Calculate the total waiting time for this combination
        wait_time = 0
        for i in range(N):
            wait_time += food_times[i][combination[i]]
        # If the total waiting time is less than the current minimum, update the minimum
        if wait_time < min_wait_time:
            min_wait_time = wait_time
    # Return the minimum total waiting time
    return min_wait_time

