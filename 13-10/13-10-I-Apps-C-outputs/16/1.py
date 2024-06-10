
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)

    # Get the number of contestants with a higher aggregate score
    num_higher_scores = len([s for s in scores if s > aggregate_score])

    # Return the rank
    return num_higher_scores + 1

def get_worst_rank(scores):
    # Get the number of contests
    n = len(scores)

    # Initialize the worst rank to 1
    worst_rank = 1

    # Loop through the contests
    for i in range(n):
        # Get the current rank
        current_rank = get_rank(scores[:i] + scores[i+1:])

        # Update the worst rank if necessary
        if current_rank > worst_rank:
            worst_rank = current_rank

    # Return the worst rank
    return worst_rank

if __name__ == '__main__':
    n, m = map(int, input().split())
    scores = []
    for i in range(m):
        scores.append(list(map(int, input().split())))
    print(get_worst_rank(scores))

