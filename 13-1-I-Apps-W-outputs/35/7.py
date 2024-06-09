
def knights_tournament(k):
    # Calculate the number of knights taking part in each round
    knights_per_round = [2 * k - i + 1 for i in range(1, k + 1)]
    
    # Initialize a list to store the number of initial configurations leading to the final
    final_configurations = [0] * (2 * k + 1)
    
    # Iterate over each round
    for i in range(1, k + 1):
        # Calculate the number of initial configurations leading to the final in the current round
        num_final_configurations = 0
        for j in range(1, 2 * k - i + 2):
            # Calculate the number of initial configurations leading to the current position in the current round
            num_configurations = knights_per_round[i - 1] // (j + 1)
            # Add the number of initial configurations leading to the current position in the current round to the total number of initial configurations leading to the final
            num_final_configurations += num_configurations
        
        # Add the number of initial configurations leading to the final in the current round to the list of final configurations
        final_configurations[i] = num_final_configurations
    
    # Return the list of final configurations
    return final_configurations

