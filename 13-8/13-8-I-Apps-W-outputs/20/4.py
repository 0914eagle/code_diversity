
def find_magical_permutation(n, s):
    # Sort the set in ascending order
    s = sorted(s)
    # Initialize the maximum length of the permutation as 0
    max_len = 0
    # Initialize the permutation as an empty list
    permutation = []
    # Iterate over the powers of 2 from 1 to 2^n - 1
    for i in range(1, 2**n):
        # Initialize a temporary permutation as an empty list
        temp_permutation = []
        # Iterate over the bits of the current power of 2
        for j in range(n):
            # If the j-th bit of the current power of 2 is 1, add the (j+1)-th element of the set to the temporary permutation
            if i & (1 << j):
                temp_permutation.append(s[j])
        # If the temporary permutation has the desired property, update the maximum length and the permutation
        if has_desired_property(temp_permutation):
            max_len = len(temp_permutation)
            permutation = temp_permutation
    # Return the maximum length and the permutation
    return max_len, permutation

def has_desired_property(permutation):
    # If the permutation has only one element, return True
    if len(permutation) == 1:
        return True
    # Iterate over the adjacent elements of the permutation
    for i in range(len(permutation) - 1):
        # If the bitwise xor of the ith and i+1-th elements is not in the set, return False
        if permutation[i] ^ permutation[i+1] not in s:
            return False
    # If all the adjacent elements have the desired property, return True
    return True

n = int(input())
s = set(map(int, input().split()))
max_len, permutation = find_magical_permutation(n, s)
print(max_len)
print(*permutation)

