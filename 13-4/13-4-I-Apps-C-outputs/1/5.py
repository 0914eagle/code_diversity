
def solve(N, M, food_preferences):
    # Initialize the minimum total waiting time to 0
    total_waiting_time = 0

    # Loop through each dog
    for dog in range(N):
        # Initialize the current dog's waiting time to 0
        current_dog_waiting_time = 0

        # Loop through each feeding bowl
        for bowl in range(M):
            # Add the time it takes for the current dog to eat from the current bowl to the current dog's waiting time
            current_dog_waiting_time += food_preferences[dog][bowl]

            # If the current dog's waiting time is greater than the total waiting time, update the total waiting time
            if current_dog_waiting_time > total_waiting_time:
                total_waiting_time = current_dog_waiting_time

    # Return the minimum total waiting time
    return total_waiting_time

