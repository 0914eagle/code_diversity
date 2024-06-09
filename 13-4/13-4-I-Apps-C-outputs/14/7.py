
def get_results(votes, k):
    # Calculate the number of votes for each candidate
    votes_count = {}
    for vote in votes:
        if vote not in votes_count:
            votes_count[vote] = 1
        else:
            votes_count[vote] += 1

    # Sort the candidates by votes and time of last vote
    sorted_candidates = sorted(votes_count.items(), key=lambda x: (-x[1], x[0]))

    # Determine the outcome for each candidate
    outcome = []
    for candidate, votes in sorted_candidates:
        if votes >= k:
            outcome.append(1)
        elif votes < k and votes > 0:
            outcome.append(2)
        else:
            outcome.append(3)

    return outcome

def main():
    n, k, m, a = map(int, input().split())
    votes = list(map(int, input().split()))
    outcome = get_results(votes, k)
    print(*outcome)

if __name__ == '__main__':
    main()

