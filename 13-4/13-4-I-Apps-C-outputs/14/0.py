
def get_candidate_outcomes(n_candidates, n_seats, n_citizens, n_voted, voted_candidates):
    # Initialize a dictionary to store the number of votes for each candidate
    votes = {}
    for i in range(1, n_candidates + 1):
        votes[i] = 0
    
    # Count the number of votes for each candidate
    for candidate in voted_candidates:
        votes[candidate] += 1
    
    # Sort the candidates by number of votes in descending order
    sorted_candidates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize the outcomes for each candidate
    outcomes = [0] * n_candidates
    
    # Set the outcomes for the top k candidates
    for i in range(n_seats):
        outcomes[sorted_candidates[i][0] - 1] = 1
    
    # Set the outcomes for the remaining candidates
    for i in range(n_seats, n_candidates):
        if votes[sorted_candidates[i][0]] == votes[sorted_candidates[i - 1][0]]:
            outcomes[sorted_candidates[i][0] - 1] = 2
        else:
            outcomes[sorted_candidates[i][0] - 1] = 3
    
    return outcomes

def main():
    n_candidates, n_seats, n_citizens, n_voted = map(int, input().split())
    voted_candidates = list(map(int, input().split()))
    outcomes = get_candidate_outcomes(n_candidates, n_seats, n_citizens, n_voted, voted_candidates)
    print(*outcomes)

if __name__ == '__main__':
    main()

