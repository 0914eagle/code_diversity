
def get_largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Iterate through the book of great achievements
    for member1, member2 in book_of_great_achievements:
        # If the members disagree, add them to the committee
        if member1 != member2:
            committee.add(member1)
            committee.add(member2)
    # Return the size of the largest possible committee
    return len(committee)

