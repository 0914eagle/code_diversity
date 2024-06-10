
def get_rank(scores):
    # Calculate the sum of the four highest scores
    sum_scores = sum(sorted(scores, reverse=True)[:4])
    return sum_scores

def get_worst_rank(n, m, scores):
    # Initialize the worst rank as 0
    worst_rank = 0
    
    # Iterate over the scores of all contestants
    for i in range(m):
        # Calculate the rank of the current contestant
        rank = get_rank(scores[i])
        
        # Update the worst rank if necessary
        if rank > worst_rank:
            worst_rank = rank
    
    # Return the worst rank
    return worst_rank

def main():
    # Read the number of contests and participants
    n, m = map(int, input().split())
    
    # Initialize the list of scores
    scores = []
    
    # Read the scores of the first n-1 contests
    for i in range(n-1):
        scores.append(list(map(int, input().split())))
    
    # Calculate the worst rank
    worst_rank = get_worst_rank(n, m, scores)
    
    # Print the worst rank
    print(worst_rank)

if __name__ == '__main__':
    main()

