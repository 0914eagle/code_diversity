
def get_winner_probability(N, M, p_list):
    # Initialize the probability of Anthony winning as 0
    probability = 0

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning the current round
        win_probability = p_list[i]

        # If Anthony wins the current round, add his probability to the total probability
        if i % 2 == 0:
            probability += win_probability

        # If Cora wins the current round, subtract 1 from the total probability
        else:
            probability -= 1

        # If the total probability becomes less than 0, set it to 0
        if probability < 0:
            probability = 0

    # Return the probability of Anthony winning the game
    return probability

