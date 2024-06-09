
def min_citizens_to_steal(votes, limak_votes):
    votes.sort(reverse=True)
    citizens_to_steal = 0
    for i in range(1, len(votes)):
        if votes[0] - votes[i] > limak_votes - votes[i]:
            citizens_to_steal += 1
        else:
            break
    return citizens_to_steal

