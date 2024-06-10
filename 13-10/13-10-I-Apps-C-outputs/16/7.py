
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)
    
    # Define the rank of the contestant
    rank = 1
    
    # Iterate through the scores and calculate the rank
    for score in scores:
        if score > aggregate_score:
            rank += 1
    
    return rank

def get_worst_rank(scores):
    # Get the rank for the given scores
    rank = get_rank(scores)
    
    # Define the worst rank
    worst_rank = 30
    
    # Check if the rank is below the worst rank
    if rank < worst_rank:
        return rank
    else:
        return worst_rank

def main():
    # Read the number of contests and participants
    n, m = map(int, input().split())
    
    # Initialize the scores list
    scores = []
    
    # Iterate through the participants
    for i in range(m):
        # Read the scores for the current participant
        scores.append(list(map(int, input().split())))
    
    # Get the worst rank for each participant
    worst_ranks = [get_worst_rank(scores[i]) for i in range(m)]
    
    # Print the worst rank
    print(max(worst_ranks))

if __name__ == '__main__':
    main()

