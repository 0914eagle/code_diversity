
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for i in range(N):
        # If the politician has disagreements, add them to the committee
        if disagreements[i]:
            committee |= set(disagreements[i])
    # Return the size of the largest committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    disagreements = [set(map(int, input().split())) for _ in range(N)]
    # Find the largest committee
    largest_committee = get_largest_committee(N, K, disagreements)
    # Print the result
    print(largest_committee)

if __name__ == '__main__':
    main()

