
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for i in range(N):
        # If the politician has at least one disagreement, add them to the committee
        if disagreements[i]:
            committee.add(i)
    # While the committee size is less than K and there are still politicians to add
    while len(committee) < K and len(committee) < N:
        # Loop through each politician and their disagreements
        for i in range(N):
            # If the politician is not in the committee and has at least one disagreement with a committee member
            if i not in committee and any(j in committee for j in disagreements[i]):
                # Add the politician to the committee
                committee.add(i)
                # Break out of the loop
                break
    # Return the size of the committee
    return len(committee)

def main():
    N, K = map(int, input().split())
    disagreements = [set(map(int, input().split())) for _ in range(N)]
    print(get_largest_committee(N, K, disagreements))

if __name__ == '__main__':
    main()

