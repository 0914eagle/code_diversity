
def get_disagreements(members, disagreements):
    # Initialize a dictionary to store the disagreements between members
    disagreement_dict = {}
    for member in members:
        disagreement_dict[member] = set()

    # Fill in the dictionary with the disagreements according to the Book of Great Achievements
    for member1, member2 in disagreements:
        disagreement_dict[member1].add(member2)
        disagreement_dict[member2].add(member1)

    return disagreement_dict

def get_largest_committee(members, disagreements, k):
    # Get the disagreements between members
    disagreement_dict = get_disagreements(members, disagreements)

    # Initialize a list to store the largest committee found so far
    largest_committee = []

    # Iterate over all possible committees of size k
    for committee in itertools.combinations(members, k):
        # Check if the committee is valid (i.e., no member agrees with less than k-1 other members)
        if all(len(disagreement_dict[member].intersection(committee)) >= k-1 for member in committee):
            # If the committee is valid, add it to the list of largest committees found so far
            largest_committee.append(committee)

    # Return the largest committee found
    return max(largest_committee, key=len)

def main():
    # Read the input
    num_members, k = map(int, input().split())
    members = list(range(num_members))
    disagreements = []
    for _ in range(num_members):
        disagreements.append(set(map(int, input().split())))

    # Find the largest committee
    largest_committee = get_largest_committee(members, disagreements, k)

    # Print the size of the largest committee
    print(len(largest_committee))

if __name__ == '__main__':
    main()

