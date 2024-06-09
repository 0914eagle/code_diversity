
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Iterate through the disagreements and add the members to the committee
    for disagreement in disagreements:
        committee |= set(disagreement)
    # Return the size of the committee
    return len(committee)

