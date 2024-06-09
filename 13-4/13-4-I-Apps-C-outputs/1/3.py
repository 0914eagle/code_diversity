
def solve(N, M, food_times):
    # Initialize a list to store the minimum time for each dog to eat
    min_times = [0] * N
    # Loop through each dog
    for i in range(N):
        # Loop through each feeding bowl
        for j in range(M):
            # If the current dog has not eaten from this bowl before, or the current bowl has a shorter time, update the minimum time for this dog
            if min_times[i] == 0 or min_times[i] > food_times[i][j]:
                min_times[i] = food_times[i][j]
    # Return the sum of the minimum times for all dogs
    return sum(min_times)

