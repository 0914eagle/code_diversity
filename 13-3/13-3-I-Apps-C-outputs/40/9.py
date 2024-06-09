
def get_min_rank(scores):
    # Initialize the minimum rank for each player as 1
    min_rank = [1] * len(scores)

    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)

    # Initialize a counter for the number of players with the same score as the current player
    same_score_count = 1

    # Iterate over the sorted scores
    for i in range(1, len(sorted_scores)):
        # If the current score is the same as the previous score, increment the counter
        if sorted_scores[i] == sorted_scores[i-1]:
            same_score_count += 1
        # Otherwise, reset the counter and update the minimum rank for the current player
        else:
            min_rank[i-1] += same_score_count
            same_score_count = 1

    return min_rank

