
def knights_tournament(k):
    # Calculate the number of knights in the tournament
    n = 2 ** k
    
    # Initialize a list to store the number of initial configurations leading to the final
    final_configurations = [0] * (n + 1)
    
    # Iterate over all possible initial configurations
    for configuration in range(1, n + 1):
        # Initialize the current configuration and the number of rounds left
        current_configuration = configuration
        rounds_left = k
        
        # Iterate over the rounds of the tournament
        while rounds_left > 0:
            # Calculate the number of knights in the current round
            num_knights = 2 ** (k - rounds_left)
            
            # Iterate over the knights in the current round
            for i in range(num_knights):
                # Calculate the indices of the two knights in the current round
                index1 = (i * 2) % n
                index2 = (i * 2 + 1) % n
                
                # Calculate the strength of the two knights in the current round
                strength1 = (current_configuration >> index1) & 1
                strength2 = (current_configuration >> index2) & 1
                
                # Determine the winner of the battle
                if strength1 > strength2:
                    # The knight with the higher strength wins the battle
                    current_configuration = (current_configuration & ~(3 << index2)) | (strength1 << index2)
                else:
                    # The knight with the lower strength wins the battle
                    current_configuration = (current_configuration & ~(3 << index1)) | (strength2 << index1)
            
            # Decrement the number of rounds left
            rounds_left -= 1
        
        # If the current configuration is the final configuration, increment the number of initial configurations leading to the final
        if current_configuration == (1 << n) - 1:
            final_configurations[configuration] += 1
    
    # Return the number of initial configurations leading to the final
    return final_configurations

