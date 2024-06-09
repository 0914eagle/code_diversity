
def get_magical_permutation(s):
    # Initialize a list to store the magical permutation
    permutation = []
    
    # Iterate through the elements of the set
    for i in range(len(s)):
        # Check if the current element is already in the permutation
        if s[i] not in permutation:
            # If not, add it to the permutation
            permutation.append(s[i])
        else:
            # If it is already in the permutation, remove it
            permutation.remove(s[i])
    
    # Return the magical permutation
    return permutation

def get_largest_magical_permutation(s):
    # Initialize a variable to store the largest magical permutation
    largest_permutation = []
    
    # Iterate through the elements of the set
    for i in range(len(s)):
        # Check if the current element is already in the permutation
        if s[i] not in largest_permutation:
            # If not, add it to the permutation
            largest_permutation.append(s[i])
        else:
            # If it is already in the permutation, remove it
            largest_permutation.remove(s[i])
    
    # Return the largest magical permutation
    return largest_permutation

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    print(get_largest_magical_permutation(s))

