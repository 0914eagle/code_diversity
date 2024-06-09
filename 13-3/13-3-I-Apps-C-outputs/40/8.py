
def get_min_rank(scores):
    # Calculate the adjusted scores by replacing any score greater than l with l
    adjusted_scores = [min(score, l) for score in scores]

    # Sort the adjusted scores in descending order
    adjusted_scores.sort(reverse=True)

    # Initialize the rank counter
    rank = 1

    # Loop through the adjusted scores and increment the rank for each unique score
    for i in range(len(adjusted_scores)):
        if i == 0 or adjusted_scores[i] != adjusted_scores[i - 1]:
            rank += 1

    return rank

