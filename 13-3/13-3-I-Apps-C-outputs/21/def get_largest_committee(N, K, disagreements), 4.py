
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
    N, K = map(int, input().split())
    disagreements = []
    for i in range(N):
        D, *disagreed_with = map(int, input().split())
        disagreements.append((i, set(disagreed_with)))
    print(get_largest_committee(N, K, disagreements))

if __name__ == "__main__":
    main()

