
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and add them to the committee
    for i in range(N):
        # If the member has not already been added to the committee, add them
        if i not in committee:
            # Get the list of members that the current member disagrees with
            disagreed_with = disagreements[i]
            # Check if any of the members that the current member disagrees with are already in the committee
            for j in disagreed_with:
                if j in committee:
                    # If any of the members that the current member disagrees with are already in the committee, remove them from the committee
                    committee.remove(j)
            # Add the current member to the committee
            committee.add(i)
    # Return the size of the committee
    return len(committee)

