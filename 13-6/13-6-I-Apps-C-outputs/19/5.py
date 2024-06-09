
def get_largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member of the party
    for member in range(N):
        # Check if the member is already in the committee
        if member not in committee:
            # If not, add the member to the committee and check if they disagree with any other members
            committee.add(member)
            for other_member in range(N):
                # If the member disagrees with the other member, add the other member to the committee
                if other_member not in committee and book_of_great_achievements[member][other_member] == 1:
                    committee.add(other_member)
    # Return the size of the largest committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    book_of_great_achievements = []
    for _ in range(N):
        book_of_great_achievements.append(list(map(int, input().split())))
    # Call the function to get the largest committee
    largest_committee = get_largest_committee(N, K, book_of_great_achievements)
    # Print the result
    print(largest_committee)

if __name__ == '__main__':
    main()

