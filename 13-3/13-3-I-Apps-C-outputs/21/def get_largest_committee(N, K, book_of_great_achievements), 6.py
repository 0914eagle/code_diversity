
def get_largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member of the party
    for member in range(N):
        # If the member is not in the committee yet,
        if member not in committee:
            # Add the member to the committee
            committee.add(member)
            # Loop through each other member of the party
            for other_member in range(member+1, N):
                # If the other member is not in the committee yet and
                if other_member not in committee and \
                   # the number of disagreements between the two members is less than or equal to K,
                   book_of_great_achievements[member][other_member] <= K:
                    # Add the other member to the committee
                    committee.add(other_member)
    # Return the size of the largest possible committee
    return len(committee)

