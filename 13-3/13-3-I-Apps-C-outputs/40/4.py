
def get_min_rank(scores):
    # Calculate the total score for each player
    total_scores = [sum(score) for score in scores]

    # Sort the players by their total score in descending order
    sorted_players = sorted(range(len(total_scores)), key=lambda k: total_scores[k], reverse=True)

    # Initialize the rank for each player
    ranks = [1] * len(total_scores)

    # Loop through the players and assign the minimum possible rank
    for i in range(len(total_scores)):
        rank = 1
        for j in range(i+1, len(total_scores)):
            if total_scores[sorted_players[i]] == total_scores[sorted_players[j]]:
                rank += 1
        ranks[sorted_players[i]] = rank

    return ranks

