
def get_longest_magical_permutation(n, s):
    # Sort the input set in ascending order
    s = sorted(s)
    # Initialize the longest magical permutation length as 0
    longest_len = 0
    # Initialize the magical permutation as an empty list
    magical_permutation = []
    # Iterate over all possible lengths of the magical permutation
    for length in range(1, 2**n):
        # Initialize the current permutation as an empty list
        current_permutation = []
        # Iterate over all possible starting indices for the magical permutation
        for start in range(2**n - length):
            # Initialize the current xor as the starting index
            current_xor = start
            # Iterate over the length of the magical permutation
            for i in range(length):
                # Calculate the next index in the permutation
                next_index = (current_xor + 1) % length
                # Check if the next index is in the input set
                if s[next_index] in s:
                    # Add the next index to the current permutation
                    current_permutation.append(next_index)
                    # Calculate the next xor
                    current_xor = s[next_index] ^ current_xor
                else:
                    # If the next index is not in the input set, break the loop
                    break
            # If the current permutation has the same length as the longest magical permutation, check if it is lexicographically larger
            if len(current_permutation) == longest_len and current_permutation > magical_permutation:
                # If it is, update the magical permutation
                magical_permutation = current_permutation
            # If the current permutation has a longer length than the longest magical permutation, update the length and the magical permutation
            elif len(current_permutation) > longest_len:
                longest_len = len(current_permutation)
                magical_permutation = current_permutation
    # Return the length of the longest magical permutation and the magical permutation
    return longest_len, magical_permutation

n = int(input())
s = set(map(int, input().split()))
longest_len, magical_permutation = get_longest_magical_permutation(n, s)
print(longest_len)
print(*magical_permutation)

