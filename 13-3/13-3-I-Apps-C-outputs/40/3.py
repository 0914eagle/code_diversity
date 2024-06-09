
def get_ranks(scores):
    # Find the maximum score for each hole
    max_scores = [max(score) for score in zip(*scores)]

    # Initialize the ranks for each player to the number of players
    ranks = [len(scores)] * len(scores)

    # Loop through each hole
    for hole in range(len(scores[0])):
        # Find the minimum score for this hole
        min_score = min(score[hole] for score in scores)

        # Update the ranks for each player who achieved this minimum score
        for i, score in enumerate(scores):
            if score[hole] == min_score:
                ranks[i] -= 1

    return ranks

