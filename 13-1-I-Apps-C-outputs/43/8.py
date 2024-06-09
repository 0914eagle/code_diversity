
def get_election_results(n_candidates, k_seats, n_citizens, a_voted, voted_for):
    # Initialize a dictionary to store the number of votes for each candidate
    votes = {}
    for i in range(n_candidates):
        votes[i + 1] = 0
    
    # Count the number of votes for each candidate
    for i in range(a_voted):
        votes[voted_for[i]] += 1
    
    # Sort the candidates by number of votes in descending order
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the outcome for each candidate
    outcome = []
    
    # Iterate through the candidates and determine their outcome
    for i in range(n_candidates):
        if sorted_votes[i][1] >= k_seats:
            outcome.append(1)
        elif sorted_votes[i][1] == 0:
            outcome.append(3)
        else:
            outcome.append(2)
    
    return outcome

