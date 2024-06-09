
def get_election_results(n_candidates, n_seats, n_voters, n_votes, votes):
    # Initialize a dictionary to store the number of votes for each candidate
    votes_count = {}
    for i in range(n_candidates):
        votes_count[i + 1] = 0
    
    # Count the number of votes for each candidate
    for vote in votes:
        votes_count[vote] += 1
    
    # Sort the candidates by the number of votes in descending order
    sorted_candidates = sorted(votes_count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the outcome of the election for each candidate
    election_outcome = []
    
    # Iterate through the candidates and determine their election outcome
    for candidate in sorted_candidates:
        if candidate[1] >= n_votes:
            election_outcome.append(1)
        elif candidate[1] < n_votes and candidate[0] <= n_seats:
            election_outcome.append(2)
        else:
            election_outcome.append(3)
    
    return election_outcome

def main():
    n_candidates, n_seats, n_voters, n_votes = map(int, input().split())
    votes = list(map(int, input().split()))
    election_outcome = get_election_results(n_candidates, n_seats, n_voters, n_votes, votes)
    print(*election_outcome)

if __name__ == '__main__':
    main()

