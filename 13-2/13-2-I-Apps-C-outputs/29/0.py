
def get_winner_probability(N, M, p_list):
    # Initialize the probability of Anthony winning as 0
    probability = 0

    # Loop through each round
    for i in range(N + M - 1):
        # Get the probability of Anthony winning the current round
        probability_current_round = p_list[i]

        # If Anthony wins the current round, he will have N - 1 points left
        # If Cora wins the current round, she will have M - 1 points left
        if i % 2 == 0:
            N -= 1
        else:
            M -= 1

        # If either Anthony or Cora has no points left, the game ends
        if N == 0 or M == 0:
            break

        # Update the probability of Anthony winning based on the probability of winning the current round
        probability += probability_current_round

    # Return the probability of Anthony winning the game
    return probability

