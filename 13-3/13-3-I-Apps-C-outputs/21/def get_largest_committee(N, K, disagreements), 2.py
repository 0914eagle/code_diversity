
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and their disagreements
    for member, disagreed_with in disagreements:
        # If the member is not in the committee yet, add them
        if member not in committee:
            committee.add(member)
        # If the member disagrees with more than K other members, remove them from the committee
        if len(committee - set(disagreed_with)) <= K:
            committee.remove(member)
    # Return the size of the largest possible committee
    return len(committee)

# Example usage
disagreements = [(0, [1, 2]), (1, [0, 2, 3]), (2, [0, 1, 4]), (3, [1, 2, 4]), (4, [2, 3])]
print(get_largest_committee(5, 3, disagreements)) # should print 3

