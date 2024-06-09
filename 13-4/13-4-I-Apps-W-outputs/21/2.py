
def get_magical_permutation(s):
    # Function to find the magical permutation
    # s: set of integers
    # return: the magical permutation as a list of integers
    permutation = []
    for i in range(len(s)):
        # Iterate through the set and add the elements to the permutation
        permutation.append(s[i])
        # Find the bitwise xor of the current element with the previous element
        # and add it to the permutation if it is in the set
        if i > 0:
            permutation.append(s[i] ^ permutation[i-1])
    return permutation

def get_largest_magical_permutation(s):
    # Function to find the largest magical permutation
    # s: set of integers
    # return: the largest magical permutation as a list of integers
    # Initialize the permutation with the first element of the set
    permutation = [s[0]]
    # Iterate through the remaining elements of the set
    for i in range(1, len(s)):
        # Find the bitwise xor of the current element with the previous element
        # and add it to the permutation if it is in the set
        if s[i] ^ permutation[-1] in s:
            permutation.append(s[i] ^ permutation[-1])
    return permutation

def main():
    # Read the input n and the set of integers S
    n = int(input())
    s = set(map(int, input().split()))
    # Find the largest magical permutation
    permutation = get_largest_magical_permutation(s)
    # Print the length of the permutation
    print(len(permutation))
    # Print the permutation
    print(*permutation)

if __name__ == '__main__':
    main()

