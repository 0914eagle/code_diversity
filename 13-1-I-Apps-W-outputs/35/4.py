
def solve(K):
    # Calculate the number of knights in the tournament
    N = 2 * K

    # Initialize a list to store the number of initial configurations that lead to the final
    final_configurations = [0] * (N + 1)

    # Iterate over all possible initial configurations
    for configuration in range(1, N + 1):
        # Initialize the current configuration and the number of rounds left
        current_configuration = configuration
        rounds_left = K

        # Iterate over the rounds of the tournament
        while rounds_left > 0:
            # Calculate the position of the two knights in the current configuration
            position_1 = current_configuration % N + 1
            position_2 = (current_configuration + 1) % N + 1

            # Calculate the strength of the two knights
            strength_1 = int(position_1 / 2) + 1
            strength_2 = int(position_2 / 2) + 1

            # Determine the winner of the battle
            if strength_1 > strength_2:
                winner = position_1
            else:
                winner = position_2

            # Update the current configuration and the number of rounds left
            current_configuration = (current_configuration - winner + N) % N
            rounds_left -= 1

        # If the current configuration is the final configuration, increment the number of initial configurations that lead to the final
        if current_configuration == 0:
            final_configurations[configuration] += 1

    # Return the number of initial configurations that lead to the final
    return final_configurations

