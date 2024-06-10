t_votes(votes):
    vote_count = {}
    for vote in votes:
        if vote != '***':
            if vote in vote_count:
                vote_count[vote] += 1
            else:
                vote_count[vote] = 1
    return vote_count

def find_winner(vote_count):
    total_votes = sum(vote_count.values())
    max_votes = max(vote_count.values())
    if max_votes > total_votes / 2:
        for candidate, votes in vote_count.items():
            if votes == max_votes:
                return candidate
    return "Runoff!"

if __name__ == '__main__':
    votes = []
    while True:
        vote = input()
        if vote == '***':
            break
        votes.append(vote)
    
    vote_count = count_votes(votes)
    winner = find_winner(vote_count)
    print(winner)
