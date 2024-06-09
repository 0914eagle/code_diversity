
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and add them to the committee
    for i in range(N):
        # If the member has not been added to the committee yet, add them
        if i not in committee:
            # Add the member to the committee
            committee.add(i)
            # Loop through the disagreements of the member
            for j in disagreements[i]:
                # If the member disagrees with someone in the committee, remove them from the committee
                if j in committee:
                    committee.remove(j)
    # Return the size of the committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    disagreements = [set(map(int, input().split())) for _ in range(N)]
    # Call the function to get the largest committee
    largest_committee = get_largest_committee(N, K, disagreements)
    # Print the result
    print(largest_committee)

if __name__ == '__main__':
    main()

