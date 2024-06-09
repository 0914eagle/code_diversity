
def get_min_rank(scores):
    # Initialize the minimum rank for each player as 1
    min_rank = [1] * len(scores)

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
                # Skip the current player
                if k == i:
                    continue

                # Get the current player's scores on the current hole
                other_hole_score = scores[k][j]

                # If the current player's score on the current hole is greater than the other player's score, update the minimum rank for the current player
                if hole_score > other_hole_score:
                    min_rank[i] += 1

    return min_rank

