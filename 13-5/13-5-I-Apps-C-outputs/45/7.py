
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and add them to the committee
    for i in range(N):
        # If the member has not been added to the committee yet, add them
        if i not in committee:
            # Get the members that the current member disagrees with
            disagreed_with = set(disagreements[i])
            # Check if there are any members in the committee that the current member disagrees with
            for member in committee:
                if member in disagreed_with:
                    # If there is, remove the member from the committee
                    committee.remove(member)
            # Add the current member to the committee
            committee.add(i)
    # Return the size of the committee
    return len(committee)

