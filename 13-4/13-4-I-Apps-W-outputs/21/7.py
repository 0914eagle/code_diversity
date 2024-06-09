
def get_magical_permutation(s):
    # Function to find the magical permutation
    # s: set of integers
    # Returns: the magical permutation as a list of integers
    permutation = []
    for i in range(len(s)):
        # Initialize the permutation with the first element of the set
        if i == 0:
            permutation.append(s[i])
        else:
            # Find the bitwise xor of the previous element and the current element
            xor = s[i] ^ permutation[i-1]
            # If the xor is in the set, add it to the permutation
            if xor in s:
                permutation.append(xor)
            # If the xor is not in the set, add the previous element to the permutation
            else:
                permutation.append(permutation[i-1])
    return permutation

def get_largest_magical_permutation(s):
    # Function to find the largest magical permutation
    # s: set of integers
    # Returns: the largest magical permutation as a list of integers
    # Initialize the permutation with the first element of the set
    permutation = [s[0]]
    for i in range(1, len(s)):
        # Find the bitwise xor of the previous element and the current element
        xor = s[i] ^ permutation[i-1]
        # If the xor is in the set, add it to the permutation
        if xor in s:
            permutation.append(xor)
        # If the xor is not in the set, add the previous element to the permutation
        else:
            permutation.append(permutation[i-1])
    return permutation

def main():
    # Read the input
    n = int(input())
    s = set(map(int, input().split()))
    # Find the largest magical permutation
    permutation = get_largest_magical_permutation(s)
    # Print the result
    print(len(permutation) - 1)
    print(*permutation)

if __name__ == '__main__':
    main()

