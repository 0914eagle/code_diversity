
def get_critic_scores(n, m, k, a):
    # Initialize the average score to 0
    avg_score = 0
    # Initialize the list of critic scores
    critic_scores = []
    # Loop through each critic and their score
    for i in range(n):
        # If this is the first critic, give them a score of m
        if i == 0:
            score = m
        # Otherwise, calculate the average score based on the previous scores
        else:
            # Get the previous scores
            prev_scores = critic_scores[:i]
            # Calculate the average score
            avg_score = sum(prev_scores) / len(prev_scores)
            # If the average score is less than or equal to the current critic's initial score, give them a score of m
            if avg_score <= a[i]:
                score = m
            # Otherwise, give them a score of 0
            else:
                score = 0
        # Add the current critic's score to the list of scores
        critic_scores.append(score)
    # Return the list of critic scores
    return critic_scores

def get_permutation(n, m, k, a):
    # Get the list of critic scores
    scores = get_critic_scores(n, m, k, a)
    # Initialize the permutation to the first critic
    permutation = [1]
    # Loop through each remaining critic
    for i in range(1, n):
        # Find the next critic with the highest score
        next_critic = scores.index(max(scores)) + 1
        # Add the next critic to the permutation
        permutation.append(next_critic)
        # Remove the next critic from the list of scores
        scores.pop(next_critic - 1)
    # Return the permutation
    return permutation

def main():
    # Read the input
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    # Get the permutation
    permutation = get_permutation(n, m, k, a)
    # Print the permutation
    print(*permutation)

if __name__ == '__main__':
    main()

