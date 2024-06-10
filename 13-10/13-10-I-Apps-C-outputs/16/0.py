
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)
    
    # Create a list of ranks and their corresponding points
    ranks = [(1, 100), (11, 24), (21, 10), (22, 22), (12, 20), (13, 18), (14, 16), (15, 15), (16, 14), (17, 13), (18, 12), (19, 11), (20, 10), (22, 9), (23, 8), (24, 7), (25, 6), (26, 5), (27, 4), (28, 3), (29, 2), (30, 1)]
    
    # Initialize the worst rank
    worst_rank = 1
    
    # Loop through the ranks and calculate the worst rank
    for rank, points in ranks:
        if aggregate_score < points:
            break
        worst_rank = rank
    
    return worst_rank

def get_worst_rank(scores):
    # Calculate the worst rank after the last contest
    worst_rank = get_rank(scores)
    
    # If the worst rank is 30 or higher, the worst rank is 29
    if worst_rank >= 30:
        worst_rank = 29
    
    return worst_rank

def main():
    # Read the number of contests and participants
    n, m = map(int, input().split())
    
    # Read the scores for each participant
    scores = []
    for _ in range(m):
        scores.append(list(map(int, input().split())))
    
    # Calculate the worst rank
    worst_rank = get_worst_rank(scores)
    
    # Print the worst rank
    print(worst_rank)

if __name__ == '__main__':
    main()

