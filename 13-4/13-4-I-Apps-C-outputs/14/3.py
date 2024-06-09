
def get_election_results(n_candidates, n_seats, n_voters, voter_data):
    # Initialize a dictionary to store the number of votes for each candidate
    votes = {}
    for i in range(1, n_candidates + 1):
        votes[i] = 0
    
    # Count the number of votes for each candidate
    for voter in voter_data:
        votes[voter] += 1
    
    # Sort the candidates by number of votes in descending order
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the outcome for each candidate
    outcome = []
    
    # Iterate through the sorted candidates and determine their outcome
    for candidate, votes in sorted_votes:
        if votes >= n_seats:
            outcome.append(1)
        elif votes == 0:
            outcome.append(3)
        else:
            outcome.append(2)
    
    return outcome

def main():
    n_candidates, n_seats, n_voters, a = map(int, input().split())
    voter_data = list(map(int, input().split()))
    outcome = get_election_results(n_candidates, n_seats, n_voters, voter_data)
    print(*outcome)

if __name__ == '__main__':
    main()

