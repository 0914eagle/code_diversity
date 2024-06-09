
def get_min_waiting_time(num_dogs, num_bowls, feeding_times):
    # Initialize a list to store the feeding times for each dog
    dog_feeding_times = []
    for i in range(num_dogs):
        dog_feeding_times.append([0] * num_bowls)
    
    # Populate the feeding times for each dog
    for i in range(num_dogs):
        for j in range(num_bowls):
            dog_feeding_times[i][j] = feeding_times[i][j]
    
    # Sort the feeding times for each dog in non-decreasing order
    for i in range(num_dogs):
        dog_feeding_times[i].sort()
    
    # Initialize a variable to store the minimum waiting time
    min_waiting_time = 0
    
    # Iterate through the dogs and calculate the waiting time for each dog
    for i in range(num_dogs):
        # Calculate the waiting time for the current dog
        waiting_time = 0
        for j in range(num_bowls):
            waiting_time += dog_feeding_times[i][j]
        
        # Update the minimum waiting time
        min_waiting_time += waiting_time
    
    return min_waiting_time

