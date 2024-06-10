
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)
    
    # Get the rank of the contestant
    rank = 1
    for score in scores:
        if score > aggregate_score:
            rank += 1
    
    return rank

def get_worst_rank(n_contests, n_participants, scores):
    # Get the worst possible rank
    worst_rank = n_contests + 1
    
    # Iterate through each contest and calculate the rank
    for i in range(n_contests):
        # Get the score for the current contest
        score = scores[i]
        
        # Calculate the rank for the current contest
        rank = get_rank(scores[:i] + scores[i+1:])
        
        # Update the worst rank if necessary
        if rank > worst_rank:
            worst_rank = rank
    
    return worst_rank

def main():
    # Read the input
    n_contests, n_participants = map(int, input().split())
    scores = [int(input()) for _ in range(n_participants)]
    
    # Calculate the worst rank
    worst_rank = get_worst_rank(n_contests, n_participants, scores)
    
    # Print the output
    print(worst_rank)

if __name__ == '__main__':
    main()

