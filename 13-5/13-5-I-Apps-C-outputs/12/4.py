
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and add them to the committee
    for i in range(N):
        # If the member has not already been added to the committee, add them
        if i not in committee:
            # Add the member to the committee
            committee.add(i)
            # Loop through the other members and remove any that agree with the current member
            for j in range(N):
                if j != i and j not in committee and (i, j) not in disagreements:
                    committee.remove(j)
    # Return the size of the committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    disagreements = []
    for i in range(N):
        D = int(input())
        disagreements.extend([(i, j) for j in map(int, input().split()) if j < N])
    # Call the function to get the largest committee
    print(get_largest_committee(N, K, disagreements))

if __name__ == '__main__':
    main()

