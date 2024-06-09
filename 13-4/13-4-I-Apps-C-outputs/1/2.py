
def get_min_waiting_time(num_dogs, num_bowls, food_times):
    # Initialize a list to store the minimum time for each dog to eat
    min_times = [0] * num_dogs
    # Loop through each dog
    for i in range(num_dogs):
        # Loop through each bowl
        for j in range(num_bowls):
            # If the current time is less than the minimum time for the dog
            if food_times[i][j] < min_times[i]:
                # Update the minimum time for the dog
                min_times[i] = food_times[i][j]
    # Return the sum of the minimum times for all dogs
    return sum(min_times)

