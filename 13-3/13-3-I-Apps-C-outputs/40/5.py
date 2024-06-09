
def get_ranks(scores):
    # Initialize the ranks for each player to 1
    ranks = [1] * len(scores)

    # Loop through each player's scores
    for i in range(len(scores)):
        # Get the current player's score
        current_score = scores[i]

        # Loop through each other player's scores
        for j in range(i+1, len(scores)):
            # Get the other player's score
            other_score = scores[j]

            # If the other player's score is lower than or equal to the current player's score, increment their rank
            if other_score <= current_score:
                ranks[j] += 1

    return ranks

