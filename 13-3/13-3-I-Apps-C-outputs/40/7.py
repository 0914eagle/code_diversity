
def get_ranks(scores):
    # Initialize the ranks for each player
    ranks = [1] * len(scores)

    # Loop through each player
    for i in range(len(scores)):
        # Get the adjusted score for the current player
        adjusted_score = scores[i]

        # Loop through each other player
        for j in range(i+1, len(scores)):
            # If the other player has a lower adjusted score, update their rank
            if scores[j] < adjusted_score:
                ranks[i] += 1

    return ranks

