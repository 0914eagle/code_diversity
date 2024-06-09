
def get_magical_permutation(S):
    # Initialize a list to store the magical permutation
    permutation = []
    
    # Iterate over the elements in S
    for i in range(len(S)):
        # Check if the current element is already in the permutation
        if S[i] not in permutation:
            # If not, add it to the permutation
            permutation.append(S[i])
        else:
            # If it is already in the permutation, remove it
            permutation.remove(S[i])
    
    # Return the magical permutation
    return permutation

def get_largest_magical_permutation(S):
    # Initialize a variable to store the largest magical permutation
    largest_permutation = []
    
    # Iterate over the elements in S
    for i in range(len(S)):
        # Check if the current element is already in the permutation
        if S[i] not in largest_permutation:
            # If not, add it to the permutation
            largest_permutation.append(S[i])
        else:
            # If it is already in the permutation, remove it
            largest_permutation.remove(S[i])
    
    # Return the largest magical permutation
    return largest_permutation

if __name__ == '__main__':
    # Read the input
    n = int(input())
    S = list(map(int, input().split()))
    
    # Get the magical permutation
    permutation = get_magical_permutation(S)
    
    # Get the largest magical permutation
    largest_permutation = get_largest_magical_permutation(S)
    
    # Print the output
    print(len(largest_permutation) - 1)
    print(*largest_permutation)

