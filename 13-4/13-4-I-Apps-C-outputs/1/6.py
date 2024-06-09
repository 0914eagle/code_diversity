
def get_min_waiting_time(num_dogs, num_bowls, feeding_times):
    # Initialize a list to store the feeding times for each dog
    dog_feeding_times = []
    for i in range(num_dogs):
        dog_feeding_times.append([])
    
    # Initialize a list to store the feeding times for each bowl
    bowl_feeding_times = [0] * num_bowls
    
    # Loop through each dog and their feeding times
    for i in range(num_dogs):
        for j in range(num_bowls):
            # If the current dog has not finished eating from the current bowl
            if feeding_times[i][j] > 0:
                # Add the current dog to the list of dogs feeding from the current bowl
                dog_feeding_times[j].append(i)
                # Subtract the current dog's feeding time from the total feeding time for the current bowl
                bowl_feeding_times[j] -= feeding_times[i][j]
    
    # Initialize a variable to store the minimum waiting time
    min_waiting_time = 0
    
    # Loop through each dog and their feeding times
    for i in range(num_dogs):
        # If the current dog has not finished eating from all bowls
        if len(dog_feeding_times[i]) < num_bowls:
            # Add the current dog's feeding time to the minimum waiting time
            min_waiting_time += feeding_times[i][-1]
    
    # Return the minimum waiting time
    return min_waiting_time

