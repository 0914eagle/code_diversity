
def get_average_score(scores, n):
    return sum(scores) / n

def get_permutation(n, m, k):
    # Initialize the permutation as a list of numbers from 1 to n
    permutation = list(range(1, n + 1))
    # Initialize the average score as the target average score
    average_score = k / n
    # Iterate through the permutation
    for i in range(n):
        # Get the current critic's score
        current_score = permutation[i]
        # Get the average score of the previous critics
        previous_average_score = get_average_score(permutation[:i], i)
        # If the current critic's score is less than or equal to the previous average score, give them a score of m
        if current_score <= previous_average_score:
            permutation[i] = m
        # Otherwise, give them a score of 0
        else:
            permutation[i] = 0
    # Return the permutation if the average score is equal to the target average score
    if get_average_score(permutation, n) == average_score:
        return permutation
    # Otherwise, return "impossible"
    else:
        return "impossible"

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    scores = list(map(int, input().split()))
    print(get_permutation(n, m, k))

