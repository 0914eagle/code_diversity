
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Iterate through the disagreements and add the members to the committee
    for i in range(N):
        for j in range(i+1, N):
            if (i, j) in disagreements or (j, i) in disagreements:
                committee.add(i)
                committee.add(j)
    # Return the size of the committee
    return len(committee)

