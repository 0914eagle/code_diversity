
def solve(N, K, A, F):
    # Calculate the maximum score that can be achieved with each member doing K sets of training
    max_scores = [0] * N
    for i in range(N):
        max_scores[i] = (A[i] - K) * F[i]

    # Sort the members by their maximum score in descending order
    sorted_members = sorted(range(N), key=lambda i: max_scores[i], reverse=True)

    # Initialize the minimum possible score to the maximum score of the first member
    min_score = max_scores[sorted_members[0]]

    # Iterate through the members in descending order of their maximum score
    for i in range(N):
        # Calculate the minimum possible score that can be achieved by assigning the current member to each food
        min_food_score = [0] * N
        for j in range(N):
            min_food_score[j] = max(min_food_score[j], (A[sorted_members[i]] - K + 1) * F[j])

        # Update the minimum possible score with the minimum score that can be achieved by assigning the current member to each food
        min_score = min(min_score, max(min_food_score))

    return min_score

