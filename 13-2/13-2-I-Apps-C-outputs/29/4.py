
def get_winner_probability(N, M, p_list):
    # Initialize the probability of Anthony winning as 0
    probability = 0

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning the current round
        current_probability = p_list[i]

        # If Anthony wins the current round, he will have N - 1 points left
        # and Cora will have M - 1 points left
        if i < N - 1:
            N -= 1
        else:
            M -= 1

        # Calculate the probability of Anthony winning the next round
        next_probability = (current_probability * (N - 1) + (1 - current_probability) * (M - 1)) / (N + M - 2)

        # Add the probability of Anthony winning the current round to the total probability
        probability += current_probability

        # Update the probability of Anthony winning the next round
        current_probability = next_probability

    # Return the probability of Anthony winning the game
    return probability

