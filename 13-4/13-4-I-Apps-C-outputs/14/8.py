
def get_election_outcome(n_candidates, n_seats, n_citizens, n_voted, votes):
    # Initialize the election outcome for each candidate
    election_outcome = [0] * n_candidates
    
    # Iterate through the votes given by the citizens who have voted
    for i in range(n_voted):
        # Get the candidate for which the current citizen has voted
        candidate = votes[i]
        
        # Check if the candidate has already been elected
        if election_outcome[candidate - 1] == 1:
            continue
        
        # Check if the candidate has a chance to be elected
        if n_voted + 1 >= n_seats:
            election_outcome[candidate - 1] = 2
        else:
            election_outcome[candidate - 1] = 1
    
    # Return the election outcome for each candidate
    return election_outcome

def main():
    # Read the input data
    n_candidates, n_seats, n_citizens, n_voted = map(int, input().split())
    votes = list(map(int, input().split()))
    
    # Get the election outcome for each candidate
    election_outcome = get_election_outcome(n_candidates, n_seats, n_citizens, n_voted, votes)
    
    # Print the election outcome
    print(*election_outcome)

if __name__ == '__main__':
    main()

