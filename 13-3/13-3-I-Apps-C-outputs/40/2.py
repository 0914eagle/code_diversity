
def get_ranks(scores):
    # Initialize the ranks for each player to 1
    ranks = [1] * len(scores)

    # Loop through each player's scores
    for i in range(len(scores)):
        # Get the current player's scores
        player_scores = scores[i]

        # Loop through each hole
        for j in range(len(player_scores)):
            # Get the current hole's score
            hole_score = player_scores[j]

            # Loop through each player again
            for k in range(len(scores)):
                # If we are not looking at the current player
                if k != i:
                    # Get the score for the current player on the current hole
                    other_hole_score = scores[k][j]

                    # If the current player's score is greater than the other player's score on the current hole
                    if hole_score > other_hole_score:
                        # Increment the current player's rank
                        ranks[i] += 1

    return ranks

