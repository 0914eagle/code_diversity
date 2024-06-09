
def largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member of the party
    for i in range(N):
        # If the member is not in the committee yet, add them and find their disagreements
        if i not in committee:
            disagreements = set()
            for j in range(N):
                if book_of_great_achievements[i][j] == 1:
                    disagreements.add(j)
            # If the number of disagreements is less than K, add the member to the committee
            if len(disagreements) < K:
                committee.add(i)
    # Return the size of the committee
    return len(committee)

