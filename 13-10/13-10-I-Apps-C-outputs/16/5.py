
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)
    
    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Initialize the rank
    rank = 1
    
    # Iterate over the sorted scores
    for i in range(len(sorted_scores)):
        # Check if the current score is equal to the aggregate score
        if sorted_scores[i] == aggregate_score:
            # If it is, return the rank
            return rank
        # Otherwise, increment the rank
        rank += 1
    
    # If the rank is not found, return 0
    return 0

def get_worst_rank(n, m, scores):
    # Initialize the worst rank
    worst_rank = 0
    
    # Iterate over the first n-1 contests
    for i in range(n-1):
        # Get the rank for the current contest
        rank = get_rank(scores[i])
        
        # Check if the rank is greater than the worst rank
        if rank > worst_rank:
            # If it is, update the worst rank
            worst_rank = rank
    
    # Return the worst rank
    return worst_rank

if __name__ == '__main__':
    n, m = map(int, input().split())
    scores = []
    for i in range(m):
        scores.append(list(map(int, input().split())))
    print(get_worst_rank(n, m, scores))

