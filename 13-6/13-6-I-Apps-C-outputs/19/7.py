
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for i in range(N):
        # If the politician is not in the committee yet, add them and their disagreements to the set
        if i not in committee:
            committee.add(i)
            committee.update(disagreements[i])
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

