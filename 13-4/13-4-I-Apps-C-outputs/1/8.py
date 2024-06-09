
def get_min_waiting_time(N, M, food_times):
    # Initialize a list to store the feeding times for each dog
    feeding_times = [0] * N

    # Loop through each dog
    for i in range(N):
        # Loop through each feeding bowl
        for j in range(M):
            # If the dog has not finished eating, update its feeding time
            if feeding_times[i] < food_times[i][j]:
                feeding_times[i] = food_times[i][j]

    # Return the sum of the feeding times minus the maximum feeding time
    return sum(feeding_times) - max(feeding_times)

