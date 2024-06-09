
def get_largest_committee(N, K, book_of_achievements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and their disagreements
    for member, disagreements in book_of_achievements:
        # If the member is not in the committee, add them and their disagreements to the committee
        if member not in committee:
            committee.add(member)
            committee.update(disagreements)
        # If the member is already in the committee, check if they have any new disagreements
        else:
            # If the member has any new disagreements, add them to the committee
            if len(committee.intersection(disagreements)) < K:
                committee.update(disagreements)
    # Return the size of the largest possible committee
    return len(committee)

