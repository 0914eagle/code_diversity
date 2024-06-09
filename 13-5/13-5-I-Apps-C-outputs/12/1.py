
def get_largest_committee(N, K, disagreements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for i in range(N):
        # If the politician has no disagreements, they are automatically added to the committee
        if not disagreements[i]:
            committee.add(i)
        # If the politician has at least one disagreement, check if they can be added to the committee
        else:
            # Loop through the politician's disagreements
            for j in disagreements[i]:
                # If the politician's disagreement is not already in the committee, they can be added
                if j not in committee:
                    committee.add(i)
                    break
    
    # Return the size of the largest possible committee
    return len(committee)

def main():
    # Read the input data
    N, K = map(int, input().split())
    disagreements = [set(map(int, input().split())) for _ in range(N)]
    
    # Call the function to get the largest possible committee
    largest_committee = get_largest_committee(N, K, disagreements)
    
    # Print the result
    print(largest_committee)

if __name__ == '__main__':
    main()

