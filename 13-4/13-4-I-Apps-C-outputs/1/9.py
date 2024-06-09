
def get_min_waiting_time(num_dogs, num_bowls, feeding_times):
    # Initialize a list to store the feeding times for each dog
    dog_feeding_times = []
    for i in range(num_dogs):
        dog_feeding_times.append([0] * num_bowls)
    
    # Initialize a list to store the feeding times for each bowl
    bowl_feeding_times = [0] * num_bowls
    
    # Loop through each dog and its feeding times
    for i in range(num_dogs):
        for j in range(num_bowls):
            # If the dog has not finished eating, add the feeding time to the bowl's total feeding time
            if feeding_times[i][j] > 0:
                bowl_feeding_times[j] += feeding_times[i][j]
            # If the dog has finished eating, add the feeding time to the dog's total feeding time
            else:
                dog_feeding_times[i][j] += feeding_times[i][j]
    
    # Find the maximum feeding time for any dog or bowl
    max_dog_feeding_time = max(max(dog_feeding_times), max(bowl_feeding_times))
    
    # Calculate the total waiting time by subtracting the maximum feeding time from the sum of all feeding times
    total_waiting_time = sum(dog_feeding_times) + sum(bowl_feeding_times) - max_dog_feeding_time * num_dogs
    
    return total_waiting_time

