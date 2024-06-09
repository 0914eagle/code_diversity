
def get_magical_permutation(n, s):
    # Sort the set in ascending order
    s = sorted(s)
    # Initialize the maximum length of the permutation as 0
    max_len = 0
    # Initialize the permutation as an empty list
    permutation = []
    # Iterate over the possible lengths of the permutation
    for len in range(1, n):
        # Iterate over the possible start indices
        for start in range(n - len + 1):
            # Check if the permutation is magical
            if is_magical(s, start, start + len):
                # If the permutation is magical, update the maximum length and the permutation
                max_len = len
                permutation = list(range(start, start + len))
    # Return the maximum length and the permutation
    return max_len, permutation

def is_magical(s, start, end):
    # Check if the range is valid
    if end - start < 2:
        return False
    # Iterate over the elements in the range
    for i in range(start, end - 1):
        # Check if the bitwise xor of the current and next element is in the set
        if s[i] ^ s[i + 1] not in s:
            return False
    return True

n = int(input())
s = set(map(int, input().split()))
max_len, permutation = get_magical_permutation(n, s)
print(max_len)
print(*permutation)

