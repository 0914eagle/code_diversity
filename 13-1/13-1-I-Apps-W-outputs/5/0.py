
def solve(N, K, A, F):
    # Calculate the maximum score that can be achieved with each member doing K sets of training
    max_scores = [0] * N
    for i in range(N):
        max_scores[i] = (A[i] - K) * F[i]

    # Sort the members by their maximum score in descending order
    sorted_members = sorted(range(N), key=lambda i: max_scores[i], reverse=True)

    # Initialize the minimum possible score to the maximum score of the best member
    min_score = max_scores[sorted_members[0]]

    # Iterate through the members in descending order of their maximum score
    for i in sorted_members:
        # If the current member's maximum score is less than the minimum possible score, break the loop
        if max_scores[i] < min_score:
            break
        # Otherwise, calculate the minimum possible score by assigning the current member to the food with the highest difficulty
        min_score = min(min_score, (A[i] - K) * F[i])

    return min_score

