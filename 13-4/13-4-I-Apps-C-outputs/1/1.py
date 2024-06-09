
def get_min_waiting_time(N, M, food_preferences):
    # Initialize a list to store the time each dog spends eating
    dog_times = [0] * N

    # Loop through each dog
    for i in range(N):
        # Loop through each bowl
        for j in range(M):
            # Add the time for the current dog to eat from the current bowl to the total time
            dog_times[i] += food_preferences[i][j]

    # Sort the dogs by their total eating time in descending order
    dog_times = sorted(dog_times, reverse=True)

    # Initialize a variable to store the minimum waiting time
    min_waiting_time = 0

    # Loop through each dog
    for i in range(N):
        # Add the time for the current dog to eat from the current bowl to the minimum waiting time
        min_waiting_time += dog_times[i]

    return min_waiting_time

