
def get_winner_probability(N, M, p_list):
    # Initialize the probability of Anthony winning as 0
    probability = 0

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning the current round
        probability_current_round = p_list[i]

        # If Anthony wins the current round, he will have N - 1 points left
        # and Cora will have M - 1 points left
        if i < N - 1:
            N -= 1
        if i < M - 1:
            M -= 1

        # Calculate the probability of Anthony winning the next round
        probability_next_round = (N - 1) / (N + M - 2)

        # Update the probability of Anthony winning
        probability += probability_current_round * probability_next_round

    # Return the probability of Anthony winning the game
    return probability

