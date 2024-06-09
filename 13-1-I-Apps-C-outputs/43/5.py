
def get_election_results(n_candidates, n_seats, n_citizens, n_voted, voted_candidates):
    # Initialize a dictionary to store the number of votes for each candidate
    votes = {}
    for i in range(n_candidates):
        votes[i + 1] = 0
    
    # Count the number of votes for each candidate
    for candidate in voted_candidates:
        votes[candidate] += 1
    
    # Sort the candidates by number of votes in descending order, and then by time of last vote in ascending order
    sorted_candidates = sorted(votes.items(), key=lambda x: (-x[1], x[0]))
    
    # Initialize a list to store the outcome for each candidate
    outcome = []
    
    # Iterate through the sorted candidates and assign an outcome based on the number of seats available
    for candidate, votes in sorted_candidates:
        if votes >= n_seats:
            outcome.append(1)
            n_seats -= 1
        elif votes == 0:
            outcome.append(3)
        else:
            outcome.append(2)
    
    return outcome

