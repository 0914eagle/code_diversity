
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and their disagreements
    for member, disagreed_with in disagreements:
        # If the member is not in the committee, add them and their disagreements to the committee
        if member not in committee:
            committee.add(member)
            committee.update(disagreed_with)
    # Return the size of the committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    disagreements = []
    for _ in range(N):
        member, D = map(int, input().split())
        disagreed_with = set(map(int, input().split()))
        disagreements.append((member, disagreed_with))
    # Call the function to get the largest committee
    largest_committee = get_largest_committee(N, K, disagreements)
    # Print the result
    print(largest_committee)

if __name__ == "__main__":
    main()

