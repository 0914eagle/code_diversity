
def get_election_outcome(n_candidates, n_seats, n_voters, n_votes, votes):
    # Initialize a dictionary to store the number of votes for each candidate
    votes_count = {}
    for i in range(n_candidates):
        votes_count[i + 1] = 0
    
    # Count the number of votes for each candidate
    for vote in votes:
        votes_count[vote] += 1
    
    # Sort the candidates by the number of votes in descending order
    sorted_candidates = sorted(votes_count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize the election outcome array
    election_outcome = [0] * n_candidates
    
    # Determine the candidates with a chance to be elected
    for i in range(n_seats):
        election_outcome[sorted_candidates[i][0] - 1] = 1
    
    # Determine the candidates with no chances to be elected
    for i in range(n_seats, n_candidates):
        election_outcome[sorted_candidates[i][0] - 1] = 3
    
    return election_outcome

def main():
    n_candidates, n_seats, n_voters, n_votes = map(int, input().split())
    votes = list(map(int, input().split()))
    election_outcome = get_election_outcome(n_candidates, n_seats, n_voters, n_votes, votes)
    print(*election_outcome)

if __name__ == '__main__':
    main()

