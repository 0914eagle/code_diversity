
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for politician, disagreed_with in disagreements:
        # If the politician is not already in the committee, add them
        if politician not in committee:
            committee.add(politician)
        # Loop through the politicians the politician disagrees with
        for disagreed_with_politician in disagreed_with:
            # If the disagreed with politician is not already in the committee, add them
            if disagreed_with_politician not in committee:
                committee.add(disagreed_with_politician)
    # Return the size of the committee
    return len(committee)

def main():
    # Read the input
    N, K = map(int, input().split())
    disagreements = []
    for i in range(N):
        D_i = int(input())
        disagreed_with = set(map(int, input().split()))
        disagreements.append((i, disagreed_with))
    # Call the function to get the largest committee
    largest_committee = get_largest_committee(N, K, disagreements)
    # Print the result
    print(largest_committee)

if __name__ == '__main__':
    main()

