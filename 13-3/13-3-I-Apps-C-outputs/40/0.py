
def get_min_rank(scores):
    # Find the maximum score among all players
    max_score = max(scores)

    # Initialize the minimum rank for each player as the number of players
    min_rank = len(scores)

    # Iterate through all possible scores
    for score in range(max_score + 1):
        # Count the number of players with a score less than or equal to the current score
        num_players = sum(1 for s in scores if s <= score)

        # Update the minimum rank for each player if the current score is better than their current minimum rank
        for i in range(len(scores)):
            if num_players < min_rank[i]:
                min_rank[i] = num_players

    return min_rank

