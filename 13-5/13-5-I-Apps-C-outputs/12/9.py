
def get_largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each member of the party
    for member in range(N):
        # If the member is not in the committee yet, add them and find their disagreements
        if member not in committee:
            disagreements = find_disagreements(member, committee, book_of_great_achievements)
            # If the number of disagreements is less than or equal to K, add the member to the committee
            if len(disagreements) <= K:
                committee.add(member)
    # Return the size of the largest committee
    return len(committee)

def find_disagreements(member, committee, book_of_great_achievements):
    # Initialize a set to store the disagreements
    disagreements = set()
    # Loop through each member of the party
    for other_member in range(len(book_of_great_achievements)):
        # If the other member is not in the committee yet and they disagree with the member, add them to the disagreements set
        if other_member not in committee and member in book_of_great_achievements[other_member]:
            disagreements.add(other_member)
    # Return the set of disagreements
    return disagreements

if __name__ == '__main__':
    N, K = map(int, input().split())
    book_of_great_achievements = []
    for _ in range(N):
        book_of_great_achievements.append(set(map(int, input().split())))
    print(get_largest_committee(N, K, book_of_great_achievements))

