
def largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and their disagreements
    for member, disagreed_with in disagreements:
        # If the member is not in the committee yet, add them
        if member not in committee:
            committee.add(member)
        # If the member already in the committee, check if they disagree with too many other members
        else:
            # If the member disagrees with too many other members, remove them from the committee
            if len(committee - set(disagreed_with)) < K:
                committee.remove(member)
    # Return the size of the largest possible committee
    return len(committee)

