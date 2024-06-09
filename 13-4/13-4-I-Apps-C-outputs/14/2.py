
def get_election_results(n_candidates, k_seats, m_voters, a_voted, g_voted):
    # Initialize a dictionary to store the number of votes for each candidate
    votes = {}
    for i in range(1, n_candidates + 1):
        votes[i] = 0
    
    # Count the number of votes for each candidate
    for i in range(a_voted):
        votes[g_voted[i]] += 1
    
    # Sort the candidates by the number of votes in descending order
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the outcome for each candidate
    outcome = []
    for i in range(n_candidates):
        if i < k_seats:
            outcome.append(1)
        elif votes[sorted_votes[i][0]] == votes[sorted_votes[i - 1][0]]:
            outcome.append(2)
        else:
            outcome.append(3)
    
    return outcome

def main():
    n_candidates, k_seats, m_voters, a_voted = map(int, input().split())
    g_voted = list(map(int, input().split()))
    outcome = get_election_results(n_candidates, k_seats, m_voters, a_voted, g_voted)
    print(*outcome)

if __name__ == '__main__':
    main()

