
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Loop through each member and add them to the committee
    for i in range(N):
        # If the member disagrees with at least K other members, add them to the committee
        if len(disagreements[i]) >= K:
            committee.add(i)
    # Return the size of the committee
    return len(committee)

def main():
    N, K = map(int, input().split())
    disagreements = []
    for i in range(N):
        D = list(map(int, input().split()))
        disagreements.append(D)
    print(get_largest_committee(N, K, disagreements))

if __name__ == "__main__":
    main()

