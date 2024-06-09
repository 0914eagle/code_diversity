
def solve(D, G, p_scores, c_scores):
    # Initialize variables
    total_score = 0
    num_problems = 0

    # Sort the p_scores and c_scores in descending order
    p_scores.sort(reverse=True)
    c_scores.sort(reverse=True)

    # Loop through the p_scores and c_scores
    for i in range(D):
        # Calculate the total score if Takahashi solves the current problem
        total_score += p_scores[i]
        num_problems += 1

        # Check if the total score is greater than or equal to G
        if total_score >= G:
            return num_problems

        # If not, calculate the perfect bonus for the current problem
        total_score += c_scores[i]

    # If we reach this point, it means that Takahashi cannot achieve the objective with the given p_scores and c_scores
    return -1

