
def get_magical_permutation(s):
    # Function to find the magical permutation
    # s: set of integers
    # Returns the magical permutation as a list of integers
    permutation = []
    for i in range(len(s)):
        # Iterate over the set of integers
        # and add the next integer to the permutation
        permutation.append(s[i])
        # Find the next integer in the set that is not in the permutation
        # and add it to the permutation
        for j in range(i+1, len(s)):
            if s[j] not in permutation:
                permutation.append(s[j])
                break
    return permutation

def get_largest_magical_permutation(s):
    # Function to find the largest magical permutation
    # s: set of integers
    # Returns the largest magical permutation as a list of integers
    permutation = []
    for i in range(len(s)):
        # Iterate over the set of integers
        # and add the next integer to the permutation
        permutation.append(s[i])
        # Find the next integer in the set that is not in the permutation
        # and add it to the permutation
        for j in range(i+1, len(s)):
            if s[j] not in permutation:
                permutation.append(s[j])
                break
        # Check if the current permutation is magical
        if is_magical_permutation(permutation, s):
            # If it is magical, return it
            return permutation
    # If no magical permutation is found, return an empty list
    return []

def is_magical_permutation(permutation, s):
    # Function to check if a permutation is magical
    # permutation: list of integers
    # s: set of integers
    # Returns True if the permutation is magical, False otherwise
    for i in range(len(permutation)-1):
        # Iterate over the permutation and check if the bitwise xor of any two consecutive elements is in the set
        if permutation[i] ^ permutation[i+1] not in s:
            return False
    return True

def main():
    # Read the input
    n = int(input())
    s = set(map(int, input().split()))
    # Find the largest magical permutation
    permutation = get_largest_magical_permutation(s)
    # Print the result
    if permutation:
        print(len(permutation)-1)
        print(*permutation)
    else:
        print(0)

if __name__ == '__main__':
    main()

