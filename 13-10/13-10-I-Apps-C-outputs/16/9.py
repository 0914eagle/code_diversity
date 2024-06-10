
def get_rank(scores):
    # Calculate the aggregate score
    aggregate_score = sum(scores)
    
    # Return the rank
    return 1 + len([s for s in scores if s > aggregate_score])

def get_worst_rank(contest_results):
    # Get the scores for the current contest
    scores = [result[0] for result in contest_results]
    
    # Get the worst rank possible
    worst_rank = get_rank(scores)
    
    # Return the worst rank
    return worst_rank

if __name__ == '__main__':
    # Read the input
    n, m = map(int, input().split())
    contest_results = []
    for i in range(m):
        scores = list(map(int, input().split()))
        contest_results.append((scores[0], scores[1:]))
    
    # Get the worst rank
    worst_rank = get_worst_rank(contest_results)
    
    # Print the result
    print(worst_rank)

